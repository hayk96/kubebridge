from fastapi import FastAPI, status, Response
from .redis_client import RedisClient
from .log import logger
import uvicorn

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
redis = RedisClient()


def http_srv():
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
        logger.error(e)


@app.get("/health", status_code=status.HTTP_200_OK)
async def health(response: Response):
    if not redis.ping_redis():
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {
            "status": "error",
            "message": "Service is unavailable due to a health-check failure"}
    return {"status": "success", "message": "Service is up and running"}
