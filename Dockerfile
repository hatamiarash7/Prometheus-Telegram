FROM python:3.10.5-slim

ARG DATE_CREATED
ARG VERSION
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

LABEL maintainer="Arash Hatami <hatamiarash7@gmail.com>"
LABEL org.opencontainers.image.created=$DATE_CREATED
LABEL org.opencontainers.image.version=$VERSION
LABEL org.opencontainers.image.authors="hatamiarash7"
LABEL org.opencontainers.image.vendor="hatamiarash7"
LABEL org.opencontainers.image.title="Telegram Handler"
LABEL org.opencontainers.image.description="Telegram bot for Prometheus"
LABEL org.opencontainers.image.source="https://github.com/hatamiarash7/Prometheus-Telegram"

RUN mkdir /sender

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc build-essential libffi-dev

WORKDIR /sender

COPY ./pyproject.toml /sender/
COPY ./poetry.lock /sender/

RUN pip install poetry && poetry config virtualenvs.create false && poetry install

RUN rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove gcc build-essential

COPY ./ /sender

EXPOSE 8127

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8127"]
