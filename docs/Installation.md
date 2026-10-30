# Installation Guide for Orbitron

Welcome to the installation guide for Orbitron. This guide will walk you through the steps required to set up and install the Orbitron Discord bot on your system.

## Table of Contents

- [Requirements](#requirements)
- [Installation Steps (Windows)](#installation-steps-windows)
    - [Main Installation Steps (Windows)](#main-installation-steps-windows)
    - [Contribution Installation Steps (Windows)](#contribution-installation-steps-windows)
- [Installation Steps (macOS/Linux)](#installation-steps-macoslinux)
    - [Main Installation Steps (macOS/Linux)](#main-installation-steps-macoslinux)
    - [Contribution Installation Steps (macOS/Linux)](#contribution-installation-steps-macoslinux)
- [Development Commands](#development-commands)

## Requirements

Before installing Orbitron, ensure that your system meets the following prerequisites:

| Requirement | Description | Version |
|-------------|-------------|---------|
| Python | Python programming language | 3.13 or higher |
| Git | Version control system | Latest |
| UV | Python package manager | Latest |
| Discord account | A Discord account and server with bot permissions | N/A |

Related Links:

- [Python Downloads](https://www.python.org/downloads/)
- [Git Downloads](https://git-scm.com/downloads/)
- [UV Documentation](https://pypi.org/project/uv/)
- [Discord](https://discord.com/)
- [Discord Developer Portal](https://discord.com/developers/applications)

## Installation Steps (Windows)

This section will guide you through the installation steps for setting up Orbitron on a Windows system.

**Note:** This guide assumes that you have already installed required software.

### Main Installation Steps (Windows)

This section will guide you to set up and install Orbitron for testing or production environments on a Windows system.

1. Clone the Orbitron repository from GitHub using Git:

```cmd
git clone https://github.com/theshadow131/orbitron.git
cd orbitron
```
2. Install the required Python packages using UV:

```cmd
uv sync --no-dev
```

3. Clone the environment configuration file:

```cmd
copy .env.example .env
```

4. Edit the `.env` file to configure your bot settings:

In the Discord Developer Portal, open your application and copy the bot token from its Bot settings. Set it as DISCORD_TOKEN in the .env file:

```env
DISCORD_TOKEN=your-bot-token-here
```

**Note:** Never share your bot token publicly, as it grants full access to your bot.

5. Run the bot:

```cmd
uv run --no-dev python -m orbitron
```

### Contribution Installation Steps (Windows)

This section will guide you to set up a development environment for contributing to Orbitron on a Windows system.

1. Follow the [Main Installation Steps (Windows)](#main-installation-steps-windows) as described above.

2. Set up pre-commit hooks for code quality and consistency:

```cmd
uv run pre-commit install
```

## Installation Steps (macOS/Linux)

This section will guide you through the installation steps for setting up Orbitron on a macOS or Linux system.

**Note:** This guide assumes that you have already installed required software. These steps will vary depending on your Linux distribution.

### Main Installation Steps (macOS/Linux)

This section will guide you to set up and install Orbitron for testing or production environments on a macOS or Linux system.

1. Clone the Orbitron repository from GitHub using Git:

```bash
git clone https://github.com/theshadow131/orbitron.git
cd orbitron
```
2. Install the required Python packages using UV:

```bash
uv sync --no-dev
```

3. Clone the environment configuration file:

```bash
cp .env.example .env
```

4. Edit the `.env` file to configure your bot settings:

Open the `.env` file with your preferred text editor to configure your bot settings.

```bash
nano .env
```

**Note:** You can use any text editor to edit the `.env` file, such as `nano`, `vim`, or a graphical text editor.

In the Discord Developer Portal, open your application and copy the bot token from its Bot settings. Set it as DISCORD_TOKEN in the .env file:

```env
DISCORD_TOKEN=your-bot-token-here
```

**Note:** Never share your bot token publicly, as it grants full access to your bot.

5. Run the bot:

```bash
uv run --no-dev python -m orbitron
```

### Contribution Installation Steps (macOS/Linux)

This section will guide you to set up a development environment for contributing to Orbitron on a macOS or Linux system.

1. Follow the [Main Installation Steps (macOS/Linux)](#main-installation-steps-macoslinux) as described above.

2. Set up pre-commit hooks for code quality and consistency:

```bash
uv run pre-commit install
```

## Development commands

This section provides commonly used development commands for Orbitron.

- Check code quality with Ruff:
```bash
uv run ruff check .
```

- Fix code quality with Ruff
```bash
uv run ruff check --fix .
```

- Check code format with ruff:
```bash
uv run ruff format --check .
```

- Fix code format with ruff:
```bash
uv run ruff format .
```

- Check code typing with mypy:
```bash
uv run mypy .
```

- Run all tests with pytest:
```bash
uv run pytest
```

- Run all pre-commit hooks:
```bash
uv run pre-commit run --all-files
```

