# POCPlayWright

Proof of Concept for Playwright testing with Python.

## Overview

This repository contains a Playwright testing setup using Python with pytest. It includes GitHub Actions workflow configuration for automated testing.

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

## Installation

1. Install dependencies:
```bash
cd POC-PW
pip install pytest playwright pytest-playwright pytest-html
```

2. Install Playwright browsers:
```bash
playwright install chromium
playwright install-deps chromium
```

## Running Tests

Execute tests locally:
```bash
cd POC-PW
pytest --html=reports/report.html --self-contained-html
```

## CI/CD with GitHub Actions

This repository uses GitHub Actions for automated testing. The workflow is configured to run on:
- Push to `main` or `master` branches
- Pull requests to `main` or `master` branches
- Manual workflow dispatch

### Self-Hosted Runner Setup

The workflow is configured to use a self-hosted runner. If you're getting registration errors, please see the comprehensive guide:

**[📖 Self-Hosted Runner Setup Guide](RUNNER_SETUP.md)**

The guide covers:
- Common registration errors and solutions
- Step-by-step setup instructions
- Troubleshooting the "NotFound" error
- Security best practices

### Using GitHub-Hosted Runners

If you prefer to use GitHub's hosted runners instead, modify `.github/workflows/playwright-tests.yml`:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest  # Change from [self-hosted, us14-acuo125]
```

## Project Structure

```
POCPlayWright/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml    # GitHub Actions workflow
├── POC-PW/
│   ├── conftest.py                 # Pytest configuration
│   ├── pytest.ini                  # Pytest settings
│   ├── pyproject.toml              # Project metadata
│   ├── tests/                      # Test files
│   └── reports/                    # Test reports
├── RUNNER_SETUP.md                 # Self-hosted runner guide
└── README.md                       # This file
```

## Troubleshooting

### Self-Hosted Runner Issues

If you encounter the error: `Http response code: NotFound from 'POST https://api.github.com/actions/runner-registration'`

This typically means:
1. Incorrect repository URL in runner configuration
2. Expired registration token
3. Insufficient repository permissions

**See [RUNNER_SETUP.md](RUNNER_SETUP.md) for detailed solutions.**

### Test Failures

1. Ensure all dependencies are installed
2. Verify Playwright browsers are installed
3. Check that tests are running from the correct directory (`POC-PW`)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure they pass
5. Submit a pull request

## License

This is a proof of concept project.
