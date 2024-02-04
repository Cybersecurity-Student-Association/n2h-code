# This example requires the 'message_content' intent.
import asyncio

import os
import random
from slashCommands import *

load_dotenv()
TOKEN = os.getenv('TOKEN')


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
