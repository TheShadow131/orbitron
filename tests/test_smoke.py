"""Smoke tests for the Orbitron Discord bot."""

from orbitron.__main__ import bot


def test_ping_command_is_registered() -> None:
    """Test that the ping command is registered."""
    assert bot.tree.get_command("ping") is not None
