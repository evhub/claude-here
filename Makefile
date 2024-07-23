.PHONY: test
test: install
	python -X dev ./test_file.py

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
	coconut claude_here --target 3 --no-tco --strict

.PHONY: build
build: clean unclean-build

.PHONY: force-build
force-build: clean
	coconut claude_here --force --target 3 --no-tco --strict

.PHONY: package
package:
	python -m pip install -U pip setuptools wheel twine importlib_metadata build
	python -m build

.PHONY: upload
upload: install package
	python -m twine upload dist/*

.PHONY: clean
clean:
	rm -rf ./dist ./build
	-find . -name "*.pyc" -delete
	-C:/GnuWin32/bin/find.exe . -name "*.pyc" -delete
	-find . -name "__pycache__" -delete
	-C:/GnuWin32/bin/find.exe . -name "__pycache__" -delete
