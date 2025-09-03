# weather-analytics

## Linting

Run flake8 to check code style:
```sh
flake8 src tests
```

## Coverage

Run tests and check coverage (minimum 80% enforced in CI):
```sh
pytest --cov=src --cov-fail-under=80
```

## GitHub Actions Workflow

See `.github/workflows/ci.yml` for the complete pipeline:
- Installs dependencies
- Runs linting (flake8)
- Runs tests with coverage
- Builds a zip artifact
- Uploads artifact
- Deploys Flask app to GitHub Pages (containerized)

## Artifact Creation

The workflow zips the project files and uploads as an artifact named `weather-analytics-artifact`.

## Deployment

The Flask app is deployed to GitHub Pages using the `gh-pages` branch via GitHub Actions.