# Imports
import os
from dotenv import load_dotenv
import asyncio
import sqlite3
import nextcord
import random

# Get Token
load_dotenv("env/.env")
TOKEN = os.getenv("TOKEN")

# Client Setup
intents = nextcord.Intents.all()
client = nextcord.Client(intents=intents)

@client.event
async def on_message(ctx):
    channel = client.get_channel(1155864913357582496)
    if ctx.author.id == 1155864047837786164:
        pass
    else:
        await channel.send(f'{ctx.author.display_name} said "{ctx.content}" in {ctx.channel}')

@client.event
async def on_ready():
    print(f"Logging in to discord.com as {client.user.name}")
    embed = nextcord.Embed(title=f"{client.user.name} is online", description="", color=0x9966CB)

@client.event
async def on_close():
    print(f"Logging out of discord.com as {client.user.name}")
    embed = nextcord.Embed(title=f"{client.user.name} is offline", description="", color=0x9966CB)

# Client Run
client.run(TOKEN)