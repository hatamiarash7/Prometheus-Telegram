.PHONY: install lock

install:
	poetry install

lock:
	poetry lock --no-update
