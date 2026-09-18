# sdet_ui

Training repository with Python, pytest, Selenium, and the Page Object Pattern.
The examples exercise difficult web pages with Selenium.

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and Python 3.10 or newer, then run:

```bash
uv sync --locked
```

Dependencies are declared in `pyproject.toml`. Commit `uv.lock` to keep installations reproducible.
Only direct dependencies are declared; uv resolves transitive dependencies into `uv.lock`.
pytest and code quality tools are in the default `dev` dependency group.
uv creates the local `.venv`; select `.venv/bin/python` as the interpreter in your IDE.

## Running tests

Install Google Chrome and run tests from the repository root:

```bash
uv run --locked pytest
```

The tests launch a visible browser, so they require a graphical session and internet access.
Selenium Manager handles ChromeDriver; its first run may need to download the driver.

To check test collection without starting a browser:

```bash
uv run --locked pytest --collect-only -q
```

## Managing dependencies

```bash
uv add package-name
uv remove package-name
```

To update dependencies within the declared version ranges:

```bash
uv lock --upgrade
uv sync --locked
```

For a new major version, update its constraint in `pyproject.toml` and verify the tests.

## Code checks and CI

After `uv sync --locked`, enable the hooks locally:

```bash
uv run --locked pre-commit install
uv run --locked pre-commit run --all-files
```

The hooks check whitespace, YAML, TOML, merge conflicts, Ruff lint and formatting,
and whether `uv.lock` matches `pyproject.toml`. Tools use the versions in `uv.lock`.
Some hooks fix files automatically; review and stage those changes before committing.

GitHub Actions runs the same checks and collects tests on Python 3.10 and 3.12
for pushes and pull requests. It also supports manual runs. CI does not execute
browser tests; run those locally in a graphical session as described above.
