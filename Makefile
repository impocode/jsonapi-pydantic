test:
	poetry run pytest . -x

style:
	poetry run ruff format
	poetry run ruff check --fix --show-fixes
