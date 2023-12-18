# Contributor Guide

Thank you for your interest in improving this project.
This project is open-source under the [MIT license](https://opensource.org/licenses/MIT) and
welcomes contributions in the form of bug reports, feature requests, and pull requests.

Here is a list of important resources for contributors:

- [Source Code](https://github.com/pauleveritt/viewdom)
- [Documentation](https://viewdom.readthedocs.io/)
- [Issue Tracker](https://github.com/pauleveritt/viewdom/issues)
- [Code of Conduct](codeofconduct)

## How to report a bug

Report bugs on the [Issue Tracker](https://github.com/pauleveritt/viewdom/issues).

When filing an issue, make sure to answer these questions:

- Which operating system and Python version are you using?
- Which version of this project are you using?
- What did you do?
- What did you expect to see?
- What did you see instead?

The best way to get your bug fixed is to provide a test case,
and/or steps to reproduce the issue.

## How to request a feature

Request features on the [Issue Tracker](https://github.com/pauleveritt/viewdom/issues).

## How to set up your development environment

You need Python 3.11+ and the following tools:

- [Hatch](https://hatch.pypa.io/latest/)

You can now run an interactive Python session,
or the command-line interface:

```shell
$ hatch shell
```

## How to test the project

Run the full test suite:

```shell
$ hatch run test:run
```

Unit tests are located in the `tests` directory,
and are written using the [pytest](https://pytest.readthedocs.io/) testing framework.

## How to set up your PyCharm environment

Get test virtualenv interpreter path from hatch:

```shell
$ hatch env find test.py3.12
```

You should set up an existing virtualenv interpreter in PyCharm with the path from the previous command.
[follow these instructions](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html) for Existing virtual environment

## How to submit changes

Open a [pull request](https://github.com/pauleveritt/viewdom/pulls) to submit changes to this project.

Your pull request needs to meet the following guidelines for acceptance:

- The Nox test suite must pass without errors and warnings.
- Include unit tests. This project maintains 100% code coverage.
- If your changes add functionality, update the documentation accordingly.

Feel free to submit early, though—we can always iterate on this.

To run linting and code formatting checks before commiting your change, you can install pre-commit as a Git hook by running the following command:

```shell
$ hatch run pre-commit:install
```

It is recommended to open an issue before starting work on anything.
This will allow a chance to talk it over with the owners and validate your approach.
