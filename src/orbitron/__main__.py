from logging import getLogger
from os import getenv

from discord import Intents, Interaction
from discord.ext.commands import Bot
from dotenv import load_dotenv

# Note: Move this logic to a separate modules in the future.

load_dotenv()

intents = Intents.default()
bot = Bot(command_prefix="!", intents=intents)
logger = getLogger(__package__)


@bot.event
async def on_ready():
    """Envent triggered when the bot is ready."""
    logger.info(f"Logged in as {bot.user}")

    await bot.tree.sync()

    logger.info("Bot is ready and command tree is synced.")


@bot.tree.command(name="ping", description="Check the bot's latency.")
async def ping(interaction: Interaction):
    """
    Responds with the bot's latency.

    :param interaction: The interaction object representing the command invocation.
    :type interaction: Interaction
    """
    await interaction.response.send_message(
        f"Pong! {bot.latency * 1000:.2f}ms", ephemeral=True
    )


if __name__ == "__main__":
    bot_token = getenv("DISCORD_TOKEN")

    if bot_token is None:
        raise ValueError(
            "DISCORD_TOKEN is not set in the environment variables."
        )

    bot.run(bot_token, root_logger=True)
