import sys
import uuid
import loguru
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.v1.api import api_router
from app.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    openapi_url=f'{settings.API_PREFIX}/openapi.json',
)


logger = loguru.logger
logger.remove()
logger.add(
    sys.stdout, format="{time} - {level} - ({extra[request_id]}) {message} ", level="DEBUG")


@app.middleware("http")
async def request_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())

    with logger.contextualize(request_id=request_id):
        logger.info("Request started")

        try:
            return await call_next(request)
        except Exception as ex:
            logger.error(f"Request failed: {ex}")
            return JSONResponse(content={"success": False}, status_code=500)
        finally:
            logger.info("Request ended")

app.include_router(api_router, prefix=settings.API_PREFIX)
