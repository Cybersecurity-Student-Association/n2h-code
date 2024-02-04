# Functions to perform various cyber commands

import discord
from discord import app_commands
import hashlib

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Slash Command
tree = app_commands.CommandTree(client)
servers = [discord.Object(id=1160247666870075422)]

# Ping Command
@tree.command(name="ping", description="Tests whether bot is online", guilds=servers)
async def ping(interaction):
    # Me!
    if interaction.user.id == 176106602833772544:
        await interaction.response.send_message("Pong!")
    else:
        await interaction.response.send_message("ERROR: Incorrect User", ephemeral=True)

# Add Command
@tree.command(name="add", description="Adds two numbers", guilds=servers)
async def add(interaction, first_num: int, second_num: int):
    await interaction.response.send_message(first_num + second_num)

# Command to send secret messages
@tree.command(name="secret_message", description="This message will self-destruct in 5 seconds", guilds=servers)
async def secret(interaction, message: str):
    await interaction.response.send_message("*This message will self destruct in 5 seconds:*\n" + message)
    interMessage = await interaction.original_response()
    for i in range(1, 5):
        await asyncio.sleep(1)
        await interMessage.edit(content="*This message will self destruct in " + str(5 - i) + " seconds:*\n" + message)
    await interMessage.edit(content="This message has self-destructed.")

# Command for MD5 hash
@tree.command(name="md5sum", description="Hash using md5", guilds=servers)
async def md5(interaction, message: str):
    message = message.encode()
    md5sum = hashlib.md5(message).hexdigest()
    await interaction.response.send_message("Here is your hashed message: \n" + md5sum)