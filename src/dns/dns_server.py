from src.utils.log import logger
from random import choice
import dnslib as dns
import socket
import json
import sys
import os

extra_dns_config = json.loads(
    os.environ.get(
        "EXTRA_DNS_CONFIG",
        '{"A": {"kubebridge.io.": ["127.0.0.1"]}, "CNAME": {"kube-bridge.io": "kubebridge.io."}}'))


class DNSServer:
    """
    Supports A and CNAME records
    """

    def __init__(self, port=53):
        self.port = port

        self.records = extra_dns_config

    def create_response(self, request):
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

        return reply

    def serve(self):
        try:
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_socket.bind(('', self.port))
            logger.debug(f"DNS Server running on port {self.port}")
            for record_type, domains in self.records.items():
                for domain, data in domains.items():
                    logger.debug(
                        "Successfully syncing DNS records", extra={
                            "domain": domain, "ips": data})

        except Exception as e:
            logger.error(f"Failed to create socket: {e}")
            sys.exit(1)

        try:
            while True:
                try:
                    data, addr = udp_socket.recvfrom(1024)
                    request = dns.DNSRecord.parse(data)
                    reply = self.create_response(request)
                    udp_socket.sendto(reply.pack(), addr)

                except Exception as e:
                    logger.error(f"Error handling DNS request: {e}")
                else:
                    logger.debug("Successfully responding to DNS query", extra={
                        "source_ip": f"{addr[0]}:{addr[1]}",
                        "domain": request.q.qname,
                        "type": dns.QTYPE[request.q.qtype]
                    })

        except KeyboardInterrupt:
            logger.error("Server shutting down...")
            udp_socket.close()
            sys.exit(0)
