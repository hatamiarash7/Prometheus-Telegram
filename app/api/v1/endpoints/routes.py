from typing import Optional, NoReturn
from fastapi import APIRouter, status, Request
from datetime import datetime

from app import schemas
from app.services import send_message
from app.utils import formatFiredAlert, formatResolvedAlert

router = APIRouter()


@router.post('/check', status_code=status.HTTP_200_OK)
async def send_plain_message(message: schemas.PlainMessageSend) -> Optional[NoReturn]:
    await send_message(message)
    return


@router.post('/alert', status_code=status.HTTP_200_OK)
async def get_alerts(alert: Request) -> Optional[NoReturn]:
    req_info = await alert.json()
    for alert in req_info['alerts']:
        status = alert['status']
        severity = alert['labels']['severity']
        summary = alert['annotations']['summary']
        description = alert['annotations']['description']
        date = datetime.strptime(alert['startsAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
        date = date.strftime('%Y-%m-%d %H:%M:%S')

        if status == 'firing':
            message = formatFiredAlert(severity, date, summary, description)
        else:
            message = formatResolvedAlert(severity, date, summary, description)

        await send_message(message)
    return
