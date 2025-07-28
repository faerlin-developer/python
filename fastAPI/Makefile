
build:
	docker build -t myapp:latest .

run:
	docker run --rm -p 8000:8000 myapp:latest

test:
	pytest -v -s

create:
	conda create -n fastapi-env python=3.11

delete:
	conda remove --name fastapi-env --all

install:
	pip install -r requirements.txt
