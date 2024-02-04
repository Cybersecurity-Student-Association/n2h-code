# This example requires the 'message_content' intent.
import asyncio

import discord
from discord import app_commands
from dotenv import load_dotenv
import os
import random

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Slash Command
tree = app_commands.CommandTree(client)
servers = [discord.Object(id=1160247666870075422)]


async def presence():
    await client.wait_until_ready()

    presence_states = [
        discord.Activity(type=discord.ActivityType.watching, name='John Hammond'),
        discord.Activity(type=discord.ActivityType.watching, name='IT Crowd'),
        discord.Activity(type=discord.ActivityType.watching, name='War Games'),
        discord.Activity(type=discord.ActivityType.watching, name='HackerSploit'),
        discord.Activity(type=discord.ActivityType.watching, name='IPSec'),
        discord.Activity(type=discord.ActivityType.watching, name='Hak5'),
        discord.Activity(type=discord.ActivityType.playing, name='on your network'),
        discord.Activity(type=discord.ActivityType.playing, name='TCM Academy'),
        discord.Activity(type=discord.ActivityType.playing, name='picoCTF'),
        discord.Activity(type=discord.ActivityType.playing, name='Hack The Box'),
        discord.Activity(type=discord.ActivityType.playing, name='TryHackMe'),
        discord.Activity(type=discord.ActivityType.watching, name='W4nna Cry?'),
        discord.Activity(type=discord.ActivityType.listening, name='Darknet Diaries'),
        discord.CustomActivity(name='Preparing for CyberForge'),
    ]

    while not client.is_closed():
        status = random.choice(presence_states)
        await client.change_presence(activity=status)
        await asyncio.sleep(3600)

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

# Command to send secret messages
@tree.command(name="secret_message", description="This message will self-destruct in 5 seconds", guilds=servers)
async def secret(interaction, message: str):
    await interaction.response.send_message("*This message will self destruct in 5 seconds:*\n" + message)
    interMessage = await interaction.original_response()
    for i in range(1, 5):
        await asyncio.sleep(1)
        await interMessage.edit(content="*This message will self destruct in " + str(5 - i) + " seconds:*\n" + message)
    await interMessage.edit(content="This message has self-destructed.")


# Run when bot is ready to run
@client.event
async def on_ready():
    print(f"Logged in.")
    client.loop.create_task(presence())
    await tree.sync(guild=discord.Object(id=1160247666870075422))

# Test command with prefix
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)
