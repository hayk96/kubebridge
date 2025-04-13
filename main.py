from src.sync import core as sync_core
from src.dns import core as dns_core
from src.utils.log import logger
import os


if __name__ == "__main__":
    app = os.environ.get("APP_NAME", "").lower()
    try:
        logger.info(f"Starting '{app}' application")
        if app == "sync":
            sync_core.service_sync()
        elif app == "dns":
            dns_core.dns_srv()
        else:
            logger.error(
                f"Invalid application name '{app}'. Please check 'APP_NAME' environment variable.")
            exit(1)
    except KeyboardInterrupt:
        logger.info(f"Shutting down '{app}' application")
        exit(0)
