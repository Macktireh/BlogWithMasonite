serve:
	python craft serve

init:
	pip install -r requirements.txt

lint:
	python -m flake8 .

format:
	black .
	make lint
