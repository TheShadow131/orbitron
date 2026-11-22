"""Entry point module."""

from os import getenv

from dotenv import load_dotenv

from orbitron.core import CustomClient


def main() -> None:
    """Entry point function."""
    load_dotenv()

    client = CustomClient()
    token = getenv("DISCORD_TOKEN")

    if not token or not token.strip():
        raise ValueError("DISCORD_TOKEN is not set or is empty.")

    client.run(token, root_logger=True)


if __name__ == "__main__":
    main()
