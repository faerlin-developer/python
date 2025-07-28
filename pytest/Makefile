
test:
	pytest -v -s

test-parameterized:
	pytest -v -s test_util.py::test_divide_parameterized

create:
	conda create -n pytest-env python=3.11

delete:
	conda remove --name pytest-env --all

install:
	pip install -r requirements.txt
