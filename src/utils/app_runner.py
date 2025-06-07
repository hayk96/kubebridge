from typing import Callable, Iterable
from .log import logger
import threading
import sys

threads = []


def thread_exec(services: Iterable[Callable[[], None]]) -> None:
    """
    Starts multiple services in separate threads.
    """
    global threads
    threads = [threading.Thread(target=svc) for svc in services]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def shutdown_handler(sig, frame) -> None:
    """
    Handles shutdown signals (SIGINT, SIGTERM)
    by terminating child threads.
    """
    logger.info("Received shutdown signal. Terminating child threads...")
    for t in threads:
        t.terminate()
    sys.exit(0)
