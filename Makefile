.PHONY: test lint

test:
	python3 -m pytest test_calculator.py -v

lint:
	python3 -m py_compile calculator.py test_calculator.py
