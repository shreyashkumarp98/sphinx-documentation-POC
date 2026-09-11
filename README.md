# Automated Sphinx Documentation POC

This project demonstrates a fully automated Sphinx documentation system that generates documentation from Python code docstrings with zero manual effort.

## Features

- **Automated Documentation Generation**: Sphinx builds docs from source code automatically
- **Zero Developer Effort**: Developers only write code with docstrings
- **PR-Based Workflow**: Documentation updates on merge to main (not on every PR)
- **Separate Documentation Branch**: Clean isolation with `gh-pages` branch
- **GitHub Actions Deployment**: No manual repository configuration needed
- **Multi-Repository Ready**: Easy to replicate across many repositories

## Project Structure

```
sphinx-documentation-POC/
├── .github/
│   └── workflows/
│       └── docs.yml          # GitHub Actions workflow
├── docs/
│   ├── source/
│   │   ├── conf.py          # Sphinx configuration
│   │   ├── index.rst       # Main documentation page
│   │   └── modules.rst     # API documentation
│   └── build/              # Generated HTML (not committed)
├── main.py                 # Example Python code with docstrings
├── pyproject.toml          # Project dependencies
├── .gitignore             # Ignores build artifacts
└── README.md              # This file
```

## How It Works

1. Developers write code with proper docstrings
2. Create a feature branch and submit a PR
3. When PR is merged to main, GitHub Actions triggers
4. Sphinx automatically generates documentation from docstrings
5. Documentation is committed to gh-pages branch
6. GitHub Pages deploys the documentation
7. Documentation is live and up-to-date

## Local Development

### Install Dependencies

```bash
# Using uv (recommended)
uv pip install -e ".[docs]"

# Or using pip
pip install -e ".[docs]"
```

### Build Documentation Locally

```bash
cd docs
uv run sphinx-build source build
```

### View Documentation

```bash
# On Linux
xdg-open build/index.html

# On macOS
open build/index.html

# On Windows
start build/index.html
```

## Example Code

The project includes example functions in `main.py` that demonstrate proper docstring formatting:

- `greet(name: str) -> str` - Generate a greeting message
- `calculate_sum(a: int, b: int) -> int` - Calculate the sum of two numbers
- `multiply(x: float, y: float) -> float` - Multiply two numbers

## GitHub Actions Workflow

The `.github/workflows/docs.yml` file handles:

1. Building Sphinx documentation
2. Committing generated docs to gh-pages branch
3. Deploying to GitHub Pages

The workflow triggers on:
- Push to main branch
- Manual workflow dispatch

## GitHub Pages Setup

1. Go to repository Settings > Pages
2. Under "Build and deployment", set Source to "GitHub Actions"
3. The workflow will automatically handle the rest

## Benefits

- **For Developers**: Zero documentation effort, just write code with docstrings
- **For Organizations**: Scalable across hundreds of repositories, consistent process
- **For Code Quality**: Encourages proper documentation, always up-to-date

## License

This is a proof-of-concept project for demonstration purposes.