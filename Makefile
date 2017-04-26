PYTHON=./env/bin/python
PIP=./env/bin/pip

all: virtualenv requirements

virtualenv:
	test -x $(PYTHON) | python3 -m venv env

requirements:
	$(PIP) install -r requirements.txt --upgrade

unittest:
	$(PYTHON) -m unittest discover test/

linttest:
	$(PYTHON) -m pylint test

lintstrdiver:
	$(PYTHON) -m pylint strdiver

startserver:
	$(PYTHON) request_handler.py 8080
