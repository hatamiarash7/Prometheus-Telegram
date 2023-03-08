ifneq (,$(wildcard ./.env))
    include .env
    export
endif


.PHONY: install lock run

install:
	poetry install

lock:
	poetry lock --no-update

run:
	uvicorn app.main:app --reload --port 8080
