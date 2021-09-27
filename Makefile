.PHONY: black flake8 ut start

all: lint ut

lint: flake8 black

black:
	black .

flake8:
	flake8 --max-line-length=100 --ignore=E203,W503 ./event ./sample

ut:
	pytest -v --capture=no --cov-config .coveragerc --cov=. --cov-report=xml --cov-report=term-missing .

start:
	python ./manage.py runserver
