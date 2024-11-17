install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pipx install dist/*.whl --force

lint:
	poetry run flake8 gendiff
