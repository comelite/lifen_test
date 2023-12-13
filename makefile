PYTHON_FILES := $(shell find . -name "*.py")

.PHONY: all format lint typecheck test

all: format lint typecheck test

format:
	black $(PYTHON_FILES)
	isort $(PYTHON_FILES)

lint:
	pylint $(PYTHON_FILES)

typecheck:
	mypy $(PYTHON_FILES)

test:
	pytest