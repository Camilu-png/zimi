# Backend Zimi API

## Setup

### Install dependencies

Is mandatory to have installed [Poetry](https://python-poetry.org/docs/#installation) in your system.

```bash
poetry install
```

#### Activate virtual environment

This step is optional, but is recommended to activate the virtual environment.

```bash
poetry shell
```

## Development

> More info about the configuration in [pyproject.toml](pyproject.toml)

### Formatting

The project uses [Black]() for formatting, and [isort]() for imports.

```bash
make format
```

### Linting

The project uses [Ruff]() for linting.

```bash
make lint
```

### Run migrations

```bash
python manage.py migrate
```

Or if you have not activated the virtual environment:

```bash
poetry run python manage.py migrate
```

### Run server

```bash
python manage.py runserver
```
