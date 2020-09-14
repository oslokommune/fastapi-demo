Serverless FastAPI app demo
===========================

Based on example at <https://mangum.io/adapter/>


## Tests

Tests are run using [tox](https://pypi.org/project/tox/): `make test`

For tests and linting we use [pytest](https://pypi.org/project/pytest/),
[flake8](https://pypi.org/project/flake8/) and
[black](https://pypi.org/project/black/).


## Run

`make run` to start up FastAPI app locally.


## Deploy

`make deploy` or `make deploy-prod`

Requires `saml2aws`
