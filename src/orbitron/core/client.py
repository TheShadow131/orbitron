"""
Client module.

Provides a custom client implementation for the bot.
"""

from logging import getLogger
from typing import Any, cast

from discord import Intents
from discord.ext.commands import Bot


class CustomClient(Bot):
    """Custom client implementation for the bot."""

    _instance: "CustomClient | None" = None

    def __new__(cls, *args: object, **kwargs: object) -> "CustomClient":
        """
        Create a new instance of the CustomClient.

        Ensures that only one instance of the CustomClient exists (singleton pattern).

        Parameters
        ----------
        *args : tuple
            Positional arguments to be passed to the Bot constructor.
        **kwargs : dict
            Keyword arguments to be passed to the Bot constructor.

        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, *args: object, **kwargs: object) -> None:
        """
        Initialize the CustomClient instance.

        Parameters
        ----------
        *args : tuple
            Positional arguments to be passed to the Bot constructor.
        **kwargs : dict
            Keyword arguments to be passed to the Bot constructor.

        """
        if hasattr(self, "_initialized"):
            return

        if not args and "command_prefix" not in kwargs:
            kwargs["command_prefix"] = "!"

        if "intents" not in kwargs:
            intents = Intents.default()
            intents.message_content = True
            kwargs["intents"] = intents

        super().__init__(*cast(Any, args), **cast(Any, kwargs))
        self._initialized = True
        self._logger = getLogger("Orbitron")

    async def on_ready(self) -> None:
        """Event handler called when the bot is ready."""
        self._logger.info("Logged in as %s", self.user)
