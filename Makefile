.PHONY: test lint

test:
	python3 -m pytest -q

lint:
	python3 -m py_compile *.py
