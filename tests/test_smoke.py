from orbitron.__main__ import bot


def test_ping_command_is_registered() -> None:
    assert bot.tree.get_command("ping") is not None
