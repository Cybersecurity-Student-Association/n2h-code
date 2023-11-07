# This example requires the 'message_content' intent.

import discord
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Slash Command
tree = app_commands.CommandTree(client)
servers = [discord.Object(id=1160247666870075422)]

# Ping Command
@tree.command(name="ping", description="Tests whether bot is online", guilds=servers)
async def ping(interaction):
    if interaction.user.id == 176106602833772544:
        await interaction.response.send_message("Pong!")
    else:
        await interaction.response.send_message("ERROR: Incorrect User", ephemeral=True)

# Add Command
@tree.command(name="add", description="Adds two numbers", guilds=servers)
async def add(interaction, first_num: int, second_num: int):
    await interaction.response.send_message(first_num + second_num)


@client.event
async def on_ready():
    print(f"")
    await tree.sync(guild=discord.Object(id=1160247666870075422))

# Test command with prefix
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)
