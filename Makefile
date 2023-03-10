install:
	poetry install

build:
	poetry build

test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

reinstal:
	pip install --user --force-reinstall dist/*.whl
.PHONI: install build publish reinstall selfcheck check