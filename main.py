# Imports
import os
from dotenv import load_dotenv
import asyncio
import sqlite3
import nextcord

# Get Token
load_dotenv("env/.env")
TOKEN = os.getenv("TOKEN")

# Client Setup
intents = nextcord.Intents.all()
client = nextcord.Client(intents=intents)

# Client Run
client.run(TOKEN)