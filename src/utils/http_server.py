from prometheus_client import make_asgi_app as metrics_app
from fastapi import FastAPI, status, Response
from .redis_client import RedisClient
from .log import logger
import uvicorn

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.mount("/metrics", metrics_app())
redis = RedisClient()


def http_srv():
    """
    Starts the HTTP server.
    """
    host, port = "0.0.0.0", 8080
    config = uvicorn.Config(
        app,
        host=host,
        port=port,
        server_header=False,
        date_header=False,
        log_config=None)
    server = uvicorn.Server(config)
    try:
        logger.info(f"HTTP server listening on {host}:{port}")
        server.run()
    except BaseException as e:
        logger.error(f"Failed to start HTTP server. {e}")


@app.get("/ready", status_code=status.HTTP_200_OK)
async def ready(response: Response):
    """
    This endpoint allows to check if the
    service is ready to accept requests.
    """
    if redis.ping_redis(
            msg="Service is ready to receive requests",
            ext_msg={"request_path": "/ready"}
    ):
        return {"status": "success",
                "message": "Service is ready to receive requests"}
    response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return {
        "status": "error",
        "message": "Service is unavailable due to a readiness failure"}


@app.get("/health", status_code=status.HTTP_200_OK)
async def health():
    """Checks if the service is healthy."""
    return {"status": "success", "message": "Service is up and running"}
