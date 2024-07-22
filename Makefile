.PHONY: install
install: build
	python -m pip install -Ue .

.PHONY: force-install
force-install: force-build
	python -m pip install -Ue .

.PHONY: setup
setup:
	python -m pip install -U setuptools wheel pip coconut-develop[watch]

.PHONY: unclean-build
unclean-build:
	coconut claude_here --no-tco --strict

.PHONY: build
build: clean unclean-build

.PHONY: force-build
force-build: clean
	coconut claude_here --force --no-tco --strict

.PHONY: package
package:
	python setup.py sdist bdist_wheel

.PHONY: upload
upload: install package
	python -m pip install -U --ignore-installed twine
	twine upload dist/*

.PHONY: clean
clean:
	rm -rf ./dist ./build
	-find . -name "*.pyc" -delete
	-C:/GnuWin32/bin/find.exe . -name "*.pyc" -delete
	-find . -name "__pycache__" -delete
	-C:/GnuWin32/bin/find.exe . -name "__pycache__" -delete
