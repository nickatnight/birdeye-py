# birdeye-py
<p align="center">
    <a href="https://github.com/nickatnight/birdeye-py/actions">
        <img alt="GitHub Actions status" src="https://github.com/nickatnight/birdeye-py/actions/workflows/main.yml/badge.svg">
    </a>
    <a href="https://codecov.io/gh/nickatnight/birdeye-py">
        <img alt="Coverage" src="https://codecov.io/gh/nickatnight/birdeye-py/branch/main/graph/badge.svg?token=QKVhAbDk1g"/>
    </a>
    <a href="https://pypi.org/project/birdeye-py/">
        <img alt="PyPi Shield" src="https://img.shields.io/pypi/v/birdeye-py">
    </a>
    <a href="https://www.python.org/downloads/">
        <img alt="Python Versions Shield" src="https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white">
    </a>
    <!-- <a href="https://birdeye-py.readthedocs.io/en/stable/"><img alt="Read The Docs Badge" src="https://img.shields.io/readthedocs/birdeye-py"></a> -->
    <a href="https://pypi.org/project/birdeye-py/">
        <img alt="Download Shield" src="https://img.shields.io/pypi/dm/birdeye-py">
    </a>
    <a href="https://github.com/nickatnight/birdeye-py/blob/main/LICENSE">
        <img alt="License Shield" src="https://img.shields.io/github/license/nickatnight/birdeye-py">
    </a>
</p>

## Features
- 🪙 **BirdEye** Only supports [standard](https://docs.birdeye.so/docs/data-accessibility-by-packages#1-standard-package) subscription api urls (package is still in active development)
- ♻️ **Retry Strategy** Sensible defaults to reliably retry/back-off fetching data from the api
- ✏️ **Code Formatting** Fully typed with [mypy](https://mypy-lang.org/) and code formatters [black](https://github.com/psf/black) / [isort](https://pycqa.github.io/isort/)
- ⚒️ **Modern tooling** using [uv](https://docs.astral.sh/uv/), [ruff](https://docs.astral.sh/ruff/), and [pre-commit](https://pre-commit.com/)
- 📥 **GitHub Actions** CI/CD to automate [everything](.github/workflows/main.yml)
- ↩️ **Code Coverage** Fully tested using tools like [Codecov](https://about.codecov.io/)
- 🐍 **Python Support** All minor [versions](https://www.python.org/downloads/) from 3.9 are supported

## Installation
```sh
$ pip install birdeye-py
```

## Usage
```python
from birdeyepy import BirdEye

client = BirdEye(api_key="your-api-key")

# DeFi

# https://public-api.birdeye.so/defi/price
client.defi.price()  # defaults to So11111111111111111111111111111111111111112

client.defi.price(
    address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ",
    include_liquidity=True,  # can also use strings 'true' or 'false'
)

# https://public-api.birdeye.so/defi/history_price
client.defi.history(time_from=1732398942, time_to=1732398961)  # defaults to So11111111111111111111111111111111111111112

client.defi.history(
    time_from=1732398942,
    time_to=1732398961,
    address="Gr11mosZNZjwpqnemXNnWs9E2Bnv7R6vzaKwJTdjo8zQ",
    address_type="token",  # or 'pair'...defaults to 'token'
    type_in_time="15m"  # default
)

# Token

# https://public-api.birdeye.so/defi/tokenlist
client.token.list_all()
```

## Documentation
Coming Soon

---

If you would like to support development efforts, tips are greatly appreciated. SOL address: HKmUpKBCcZGVX8RqLRcKyjYuY23hQHwnFSHXzdon4pCH
