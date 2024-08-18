.PHONY: test
test: install
	pytest --strict-markers -s ./claude_here/tests.py

.PHONY: launch-fib
launch-fib: install
	python ./claude_here/test_files/fib_test.py

.PHONY: install
install: build
	python -m pip install -Ue .

.PHONY: force-install
force-install: force-build
	python -m pip install -Ue .

.PHONY: init
init:
	python -m pip install -U coconut-develop[watch]

.PHONY: setup
setup: clean
	python -m pip install -U pip setuptools wheel pytest

.PHONY: build
build: setup
	coconut claude_here --target 3.9 --no-tco --strict

.PHONY: force-build
force-build: setup
	coconut claude_here --force --target 3.9 --no-tco --strict

.PHONY: package
package: install
	python -m pip install -U pip setuptools wheel twine importlib_metadata build
	python -m build

.PHONY: upload
upload: package
	python -m twine upload dist/*

.PHONY: clean
clean:
	rm -rf ./dist ./build ./claude_here/__coconut_cache__
	-find . -name "*.pyc" -delete
	-find . -name "__pycache__" -delete
