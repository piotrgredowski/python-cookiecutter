# {{ cookiecutter.project_name }}

{%- if cookiecutter.service_or_package == "package" -%}
[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}?style=flat-square)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug}}?style=flat-square)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/)
[![PyPI - License](https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}?style=flat-square)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}/)
{%- endif %}

---

**Documentation**: [https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug}}](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug}})

**Source Code**: [https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

{% if cookiecutter.service_or_package == "package" -%}
**PyPI**: [https://pypi.org/project/{{ cookiecutter.project_slug }}/](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
{% endif %}
---

{{ cookiecutter.project_short_description }}

{% if cookiecutter.service_or_package == "package" -%}
## Installation

```sh
pip install {{ cookiecutter.project_slug }}
```
{%- endif -%}

## Development

* Clone this repository
* Requirements:
  * [Poetry](https://python-poetry.org/) {{cookiecutter.poetry_version}}
  * Python 3.7+
* Create a virtual environment and install the dependencies

```sh
poetry install
```

* Activate the virtual environment

```sh
poetry shell
```

### Testing

```sh
poetry run pytest
```

### Documentation

The documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings
 of the public signatures of the source code. The documentation is updated and published as a [Github project page
 ](https://pages.github.com/) automatically.

{%- if cookiecutter.service_or_package == "package" -%}
### Releasing

Trigger the [Draft release workflow](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/draft_release.yml)
(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.

Find the draft release from the
[GitHub releases](https://github.com/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}/releases) and publish it. When
 a release is published, it'll trigger [release](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/blob/master/.github/workflows/release.yml) workflow which creates PyPI
 release and deploys updated documentation.
{%- endif %}

### Pre-commit

Pre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality
 checks to make sure the changeset is in good shape before a commit/push happens.

You can install the hooks with (runs for each commit):

```sh
pre-commit install
```

Or if you want them to run only for each push:

```sh
pre-commit install -t pre-push
```

Or if you want e.g. want to run all checks manually for all files:

```sh
pre-commit run --all-files
```
