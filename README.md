# ViewDOM: Component-Driven Development for Python

[![Coverage Status][codecov-badge]][codecov-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]
[![PyPI][pypi-badge]][pypi-link]
[![Python Version][pypi-badge]][pypi-link]
[![PyPI - Downloads][install-badge]][install-link]
[![License][license-badge]][license-link]
[![Test Status][tests-badge]][tests-link]
[![pre-commit][pre-commit-badge]][pre-commit-link]
[![black][black-badge]][black-link]

[codecov-badge]: https://codecov.io/gh/pauleveritt/viewdom/branch/main/graph/badge.svg
[codecov-link]: https://codecov.io/gh/pauleveritt/viewdom
[rtd-badge]: https://readthedocs.org/projects/viewdom/badge/?version=latest
[rtd-link]: https://viewdom.readthedocs.io/en/latest/?badge=latest
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/ambv/black
[pypi-badge]: https://img.shields.io/pypi/v/viewdom.svg
[pypi-link]: https://pypi.org/project/viewdom
[install-badge]: https://img.shields.io/pypi/dw/viewdom?label=pypi%20installs
[install-link]: https://pypistats.org/packages/viewdom
[license-badge]: https://img.shields.io/pypi/l/viewdom
[license-link]: https://opensource.org/licenses/MIT
[tests-badge]: https://github.com/pauleveritt/viewdom/workflows/Tests/badge.svg
[tests-link]: https://github.com/pauleveritt/viewdom/actions?workflow=Tests
[pre-commit-badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-link]: https://github.com/pre-commit/pre-commit

ViewDOM brings modern frontend templating patterns to Python:

- [tagged](https://github.com/jviide/tagged) to have language-centered templating (like JS tagged templates)
- [htm](https://github.com/jviide/htm.py) to generate virtual DOM structures from a template run (like the `htm` JS package)
- ViewDOM for components which render a VDOM to a markup string, along with other modern machinery
- Optionally, [Hopscotch](https://github.com/pauleveritt/hopscotch) for a component registry with dependency injection

## Features

- Component-driven development.
- Intermediate VDOM.
- Pass in data either via props (simple) or DI (rich).
- Emphasis on modern Python dev practices: explicit, type hinting,
  static analysis, testing, docs, linting, editors.

## Requirements

- Python 3.9+.
- viewdom
- tagged
- htm.py
- Markupsafe

## Installation

You can install ViewDOM via [pip](https://pip.pypa.io/) from [PyPI](https://pypi.org/):

```shell
$ pip install viewdom
```

## Quick Examples

# Contributing

Contributions are very welcome.
To learn more, see the [contributor's guide](contributing).

# License

Distributed under the terms of the [MIT license](https://opensource.org/licenses/MIT), ViewDOM is free and open source software.

# Issues

If you encounter any problems,
please [file an issue](https://github.com/pauleveritt/viewdom/issues) along with a detailed description.

# Credits

This project was generated from [@cjolowicz's](https://github.com/cjolowicz) [Hypermodern Python Cookiecutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python) template.
