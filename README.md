# sdet_ui

Training repository with Python, pytest, Selenium, and the Page Object Pattern.
The examples exercise difficult web pages with Selenium.

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and Python 3.10 or newer, then run:

```bash
uv sync --locked
```

Dependencies are declared in `pyproject.toml`. Commit `uv.lock` to keep installations reproducible.
The migration preserves all versions from the former `requirements.txt`, including transitive dependencies.
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

To intentionally update the pinned dependencies, change their version constraints in
`pyproject.toml`, then run `uv lock` and `uv sync --locked`.
