import feedparser
from slashCommands import client
from datetime import datetime, timedelta
from discord.ext import tasks
import pytz

class RSSParser:
    # Constructor
    def __init__(self):
        self.url = "https://feeds.feedburner.com/TheHackersNews"
        self.rssSendMessage.start()

    # Function to send rss updates to channel
    @tasks.loop(hours=12)
    async def rssSendMessage(self):
        feed = feedparser.parse(self.url)

        now = datetime.now().astimezone(pytz.utc)
        time_range = timedelta(hours=12)

        for entry in feed.entries:
            entry_time = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z").astimezone(pytz.utc)

            discMessageString = ""
            if now - entry_time <= time_range:
                discMessageString = f"**{entry.title}**\n{entry.link}\n*{entry.summary}*"
                channel = client.get_channel(1160247667780235337)
                await channel.send(discMessageString)
