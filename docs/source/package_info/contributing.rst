Contributing to BirdEye Python
==============================

BirdEye Python is an open-source project and contributions are always welcome. The project has strict linting rules, so please be sure to following existing patterns and conventions.


Setting Up Your Development Environment
---------------------------------------

.. note::

    This section assumes you have Python 3.9+ installed on your system, and `uv <https://docs.astral.sh/uv/getting-started/installation/>`_ Python package manager.

To get started, fork the `birdeye-py` repository on GitHub and clone your fork locally. Then, create a virtual environment and install the project dependencies:

.. code-block:: bash

    $ uv venv
    $ uv sync

Running Tests
-------------

The project uses ``pytest`` for testing. To run the test suite, use the following command:

.. code-block:: bash

    $ make test

Linting
-------

The project uses a combination of modern tooling for linting. To run the linter, use the following command:

.. code-block:: bash

    $ make lint-all  # runs black, isort, ruff, mypy
