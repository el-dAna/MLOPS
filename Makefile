install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_example.py

format:
	black *.py


lint:
	pylint --disable=R,C example.py

all: install lint test