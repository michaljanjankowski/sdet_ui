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
Google and YouTube cookie consent is dismissed through the visible controls.
If Google returns its CAPTCHA/unusual traffic page, the Google search test is skipped
with an explicit reason; missing results or other errors still fail the test.
Use `uv run --locked pytest -ra` to display skip reasons.
Selenium Manager handles ChromeDriver; its first run may need to download the driver.

Each test gets a fresh Chrome session. To run without a visible window, use:

```bash
uv run --locked pytest --headless
```

Tests can be divided between parallel worker processes with pytest-xdist:

```bash
# Pick the number of workers automatically
uv run --locked pytest --headless -n auto

# Use an explicit limit, which is safer on machines with little memory
uv run --locked pytest --headless -n 2
```

Each worker starts its own isolated Chrome sessions. A higher worker count uses more
CPU and memory, so start with two workers and increase it only when the machine has
enough resources. Use `-n 0` or omit `-n` when debugging a single test.

When a test fails, pytest writes a screenshot and the page HTML to `test-results/`.

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

GitHub Actions runs the same checks and splits the stable The Internet browser tests
between two headless Chrome workers on Python 3.10 and 3.12. Failed runs upload screenshots and page
HTML as a `selenium-failures-*` artifact. Google and YouTube tests remain local
because those services can block automation or change independently of this project.
