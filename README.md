# Prometheus-Telegram

[![Telegram Handler](https://github.com/hatamiarash7/Prometheus-Telegram/actions/workflows/Publish.yml/badge.svg)](https://github.com/hatamiarash7/Prometheus-Telegram/actions/workflows/Publish.yml)

It's a simple API to handle alert requests and send them via Telegram.

## How-to use

1. Create a Telegram bot using [botfather](https://t.me/botfather)
2. Keep `BOT TOKEN` for later
3. Get your `API ID` and `API Hash` from [Telegram Website](https://core.telegram.org/api/obtaining_api_id)
4. Add these 3 values to `config.py` and `config/settings.py`

   ```py
   class Settings(BaseSettings):
      ...
      TG_BOT_TOKEN: str = '291043804:AAGHDLwaXNN2U2oI0uxCR35KsivsxNUqT3o'
      TG_API_ID: str = '45491'
      TG_API_HASH: str = '12e2adfabe4fb77970b6bae2823taf92'
      ...
    ```

5. Build image

    ```bash
    docker build -t prom-telegram .
    ```

6. Run image

    ```bash
    docker container run -d -p 8080:8080 prom-telegram
    ```

7. Use [alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) to send alerts using webhook to `http://<IP>:8080/get_alerts` URL
