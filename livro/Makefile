all: serve

build:
	mkdocs build

install: requirements
	pip install --upgrade setuptools
	pip3 install -r requirements.txt

serve:
	mkdocs serve
