.PHONY: default
default: pretty validate ;

.PHONY: validate
validate:  ## Прогон валидаторов
	poetry run ruff check
	poetry run toml-sort --check pyproject.toml
	make mypy

pretty:  ## "Причесать" код
	poetry run ruff format .  # Чтобы check не ругался на длинные строки
	poetry run ruff check --fix
	poetry run ruff format .  # Чтобы прибраться после check --fix
	poetry run toml-sort --in-place --all pyproject.toml