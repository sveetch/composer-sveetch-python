PYTHON_INTERPRETER=python3
VENV_PATH=.venv
PIP=$(VENV_PATH)/bin/pip

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install             -- to install this project with virtualenv and Pip"
	@echo
	@echo "  clean               -- to clean EVERYTHING (Warning)"
	@echo "  clean-install       -- to clean Python side installation"
	@echo "  clean-pycache       -- to remove all __pycache__, this is recursive from current directory"
	@echo

clean-pycache:
	rm -Rf .pytest_cache
	find . -type d -name "__pycache__"|xargs rm -Rf
	find . -name "*\.pyc"|xargs rm -f
.PHONY: clean-pycache

clean-install:
	rm -Rf $(VENV_PATH)
.PHONY: clean-install

clean: clean-install clean-pycache
.PHONY: clean

venv:
	virtualenv -p $(PYTHON_INTERPRETER) $(VENV_PATH)
.PHONY: venv

install: venv
	$(PIP) install -r requirements.txt
.PHONY: install
