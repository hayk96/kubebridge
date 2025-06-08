from src.utils.log import logger
from src.utils import metrics
from random import choice
import dnslib as dns
import socket
import time
import json
import sys
import os


def load_extra_dns_config() -> dict:
    """
    Loads extra DNS records from environment variable
    """

    default_extra_config = """
        {
          "A": {
            "kubebridge.io.": [
              "127.0.0.1"
            ]
          },
          "CNAME": {
            "kube-bridge.io": "kubebridge.io."
          }
        }
    """
    try:
        extra_dns_config = json.loads(
            os.environ.get(
                "EXTRA_DNS_CONFIG",
                default_extra_config))
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse 'EXTRA_DNS_CONFIG'. {e}")
        sys.exit(1)

    return extra_dns_config


class DNSServer:
    """
    A DNS server that supports
    "A" and "CNAME" type of records
    """

    def __init__(self, port=53):
        self.port = port

        self.records = load_extra_dns_config()

    def create_response(self, request):
        start_time = time.perf_counter()
        reply = dns.DNSRecord(
            dns.DNSHeader(
                id=request.header.id,
                qr=1,
                aa=1,
                ra=1),
            q=request.q)
        qname = str(request.q.qname)
        qtype = dns.QTYPE[request.q.qtype]

        if qtype == 'A' and qname in self.records['A']:
            ips = list(self.records['A'][qname])
            reply.add_answer(
                dns.RR(
                    qname,
                    dns.QTYPE.A,
                    rdata=dns.A(
                        choice(ips)),
                    ttl=60))

        elif qtype == 'CNAME' and qname in self.records['CNAME']:
            reply.add_answer(
                dns.RR(
                    qname,
                    dns.QTYPE.CNAME,
                    rdata=dns.CNAME(
                        self.records['CNAME'][qname]),
                    ttl=60))
        end_time = time.perf_counter()
        exec_time = end_time - start_time
        return reply, exec_time

    def serve(self):
        try:
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_socket.bind(('', self.port))
            logger.info(f"DNS server running on port {self.port}")
            for record_type, domains in self.records.items():
                for domain, data in domains.items():
                    logger.debug(
                        "Successfully syncing DNS records",
                        extra={
                            "domain": domain,
                            "record_type": record_type,
                            "ips": data})

        except Exception as e:
            logger.error(f"Failed to create socket: {e}")
            sys.exit(1)

        try:
            while True:
                try:
                    data, addr = udp_socket.recvfrom(1024)
                    request = dns.DNSRecord.parse(data)
                    reply, exec_time = self.create_response(request)
                    udp_socket.sendto(reply.pack(), addr)

                except Exception as e:
                    logger.error(f"Failed to handle DNS request: {e}")
                else:
                    logger.debug("Responding to DNS query", extra={
                        "source_ip": addr[0],
                        "domain": request.q.qname,
                        "record_type": dns.QTYPE[request.q.qtype],
                        "lookup_time_ms": (exec_time * 1000).__round__(3)
                    })

                    metrics.kubebridge_dns_lookup_time_seconds.labels(
                        app_name="dns",
                        record_type=dns.QTYPE[request.q.qtype],
                        record_name=request.q.qname,
                        record_ip=reply.short()).observe(exec_time)

        except KeyboardInterrupt:
            logger.error("Server shutting down...")
            udp_socket.close()
            sys.exit(0)
