import discord
import os
from dotenv import load_dotenv

load_dotenv()

# initiate discord client
client = discord.Client()


# discord event to check when the bot is online
@client.event
async def on_ready():
    print(f'{client.user} is now online!')


@client.event
async def on_message(message):
    # make sure bot doesn't respond to it's own messages to avoid infinite loop
    if message.author == client.user:
        return
    # lower case message
    message_content = message.content.lower()
    if message.content.startswith('get resources'):
        await message.reply("Hello I'm resources bot")


client.run(os.getenv('TOKEN'))
