from src.utils.app_runner import process_exec, shutdown_handler
from src.utils.http_server import http_srv
from src.sync import core as sync_core
from src.dns import core as dns_core
from src.utils.log import logger
import signal
import sys
import os


if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdown_handler)
    app = os.environ.get("APP_NAME", "").lower()
    logger.info(f"Starting '{app}' application")

    try:
        if app == "sync":
            process_exec((http_srv, sync_core.service_sync))
        elif app == "dns":
            process_exec((http_srv, dns_core.dns_srv))
        else:
            logger.error(
                f"Invalid application name '{app}'. Please check 'APP_NAME' environment variable.")
            sys.exit(1)
    except Exception as e:
        logger.exception(f"Unhandled exception: {e}")
        sys.exit(1)
