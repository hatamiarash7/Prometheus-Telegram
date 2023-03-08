import sys
import uuid
import logging
import loguru
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.v1.api import api_router
from app.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    openapi_url=f"{settings.API_PREFIX}/openapi.json",
)


class EndpointFilter(logging.Filter):
    """Filter endpoint logs and ignore health check"""

    def filter(self, record: logging.LogRecord) -> bool:
        return record.args and len(record.args) >= 3 and record.args[2] != "/health"


logging.getLogger("uvicorn.access").addFilter(EndpointFilter())

logger = loguru.logger
logger.remove()
logger.add(
    sys.stdout,
    format="{time} - {level} - ({extra[request_id]}) {message} ",
    level="DEBUG"
)


@app.middleware("http")
async def request_middleware(request: Request, call_next):
    if request.url.path != "/health":
        return await call_next(request)

    request_id = str(uuid.uuid4())

    with logger.contextualize(request_id=request_id):
        logger.info("Request started")

        try:
            response = await call_next(request)
            logger.info("Request ended")
            return response
        except Exception as ex:
            logger.error(f"Request failed: {ex}")
            return JSONResponse(content={"success": False}, status_code=500)

app.include_router(api_router, prefix=settings.API_PREFIX)


# Health check endpoint
@app.get('/health')
def health_check():
    return {"status": "ok"}
