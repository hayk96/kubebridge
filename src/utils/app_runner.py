from typing import Callable, Iterable
from multiprocessing import Process
import threading
from .log import logger
import sys

processes = []


def process_exec(services: Iterable[Callable[[], None]]) -> None:
    """
    Starts multiple services in separate processes.
    """
    global processes
    processes = [Process(target=svc) for svc in services]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

def process_exec_thread(services: Iterable[Callable[[], None]]) -> None:
    """
    Starts multiple services in separate processes.
    """
    global processes
    processes = [threading.Thread(target=svc) for svc in services]
    for p in processes:
        p.start()
    for p in processes:
        p.join()


def shutdown_handler(sig, frame) -> None:
    """
    Handles shutdown signals (SIGINT, SIGTERM)
    by terminating child processes.
    """
    logger.info("Received shutdown signal. Terminating child processes...")
    for p in processes:
        p.terminate()
    sys.exit(0)
