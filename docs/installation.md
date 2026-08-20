# Installation

This guide explains how to prepare the environment and run the project locally.

## Table of contents

- [Requirements](#requirements)
- [Installing requirements on Windows](#installing-requirements-on-windows)
  - [Installation with graphical installers (recommended)](#installation-with-graphical-installers-recommended)
  - [Installation with CLI](#installation-with-cli)
- [Installing requirements on Linux](#installing-requirements-on-linux)
  - [Debian/Ubuntu (CLI)](#debianubuntu-cli)
- [Getting started](#getting-started)
  - [Clone the repository](#clone-the-repository)
  - [Install dependencies with UV](#install-dependencies-with-uv)
  - [Configuration](#configuration)
  - [Startup](#startup)

## Requirements

| Requirement | Recommended version | Required | Official website | Notes |
| --- | --- | --- | --- | --- |
| Python | 3.13 or later | Yes | https://www.python.org/ | The project declares compatibility with Python >=3.13. |
| Git | Latest stable | Yes | https://git-scm.com/ | Required to clone the repository. |
| UV | Latest stable compatible with Python 3.13+ | Yes | https://docs.astral.sh/uv/ | Used to install dependencies and run the project. |

## Installing requirements on Windows

Install core system tools first, then continue with project setup.

### Installation with graphical installers (recommended)

1. Install Python from the official installer.
2. During installation, enable the option to add Python to PATH.
3. Install Git from the official installer.
4. Install UV using the official Windows guide.

Reference links:

- Python: https://www.python.org/downloads/windows/
- Git: https://git-scm.com/download/win
- UV: https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2

### Installation with CLI

PowerShell:

```powershell
winget install --id Python.Python.3.13 -e
winget install --id Git.Git -e
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Command Prompt (CMD):

```bat
winget install --id Python.Python.3.13 -e
winget install --id Git.Git -e
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation in a new terminal:

```powershell
python --version
git --version
uv --version
```

## Installing requirements on Linux

### Debian/Ubuntu (CLI)

Update package index:

```bash
sudo apt update
```

Install Python:

```bash
sudo apt install -y python3.13
```

Install Git:

```bash
sudo apt install -y git
```

Install UV:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

Restart the terminal and verify versions:

```bash
python3.13 --version
git --version
uv --version
```

## Getting started

### Clone the repository

<!-- Template note (post-clone):
Action: Replace the repository URL and project directory name with your own values.
-->

```bash
git clone https://github.com/TheShadow131/python_template.git
cd python_template
```

### Install dependencies with UV

Choose the command based on the target environment:

Production installation (main dependencies only):

```bash
uv sync --no-dev
```

Development installation (main dependencies and development tools):

```bash
uv sync
```

Install pre-commit hooks for local checks:

```bash
uv run pre-commit install
```

Verify the interpreter inside the virtual environment:

```bash
uv run python --version
```

### Configuration

<!-- Template note (post-clone):
Action: Remove this section if your project does not use environment variables.
Action: If you keep this section, document required variables and their purpose.
Action: Add an `.env.example` file without secrets.
-->

If your project includes `.env.example`, copy it locally:

```bash
cp .env.example .env
```

### Startup

Run the project with the current entry point:

```bash
uv run python -m app
```
