import os
import discord
from datetime import datetime

from hash import encrypt_string

TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

def start():
    client.run(TOKEN)

@client.event
async def on_ready():
    print(f'Connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    plain_text = message.content + message.author.name + str(message.author.id) + str(datetime.today())
    encrypted_text = encrypt_string(plain_text)
    response = "Hash: " + encrypted_text

    await message.channel.send(response)
