from typing import Optional, NoReturn
from fastapi import APIRouter, status, Request
from datetime import datetime

from app import schemas
from app.services import send_message
from app.utils import format_alert

router = APIRouter()


@router.post('/test', status_code=status.HTTP_200_OK)
async def send_plain_message(message: schemas.PlainMessageSend) -> Optional[NoReturn]:
    await send_message(message)


@router.post('/alert', status_code=status.HTTP_200_OK)
async def get_alerts(req: Request) -> Optional[NoReturn]:
    try:
        req_info = await req.json()
        alerts = req_info.get('alerts', [])
    except Exception:
        return

    for alert_data in alerts:
        status = alert_data.get('status')
        labels = alert_data.get('labels', {})
        annotations = alert_data.get('annotations', {})
        severity = labels.get('severity')
        summary = annotations.get('summary')
        description = annotations.get('description')
        starts_at = alert_data.get('startsAt')

        if not all([status, severity, summary, description, starts_at]):
            continue

        try:
            date = datetime.fromisoformat(starts_at.replace("Z", "+00:00"))
        except ValueError:
            continue

        message = format_alert(
            status == 'firing',
            severity,
            date.strftime('%Y-%m-%d %H:%M:%S'),
            summary,
            description
        )

        await send_message(message)
    return
