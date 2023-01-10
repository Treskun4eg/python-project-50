install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 gendiff

package-reinstal:
	pip install --user --force-reinstall dist/*.whl
.PHONI: install build publish reinstall