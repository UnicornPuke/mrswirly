# Imports
import os
from dotenv import load_dotenv
import nextcord
import random

# Get Token
load_dotenv("env/.env")
TOKEN = os.getenv("TOKEN")

# Client Setup
intents = nextcord.Intents.all()
client = nextcord.Client(intents=intents)

# /help
@client.slash_command(name="help", description="Helps you in this strange, strange world.")
async def hyelp(ctx):
    embed = nextcord.Embed(title="Help Menu", description="Whatcha need?", color=0x9966CB)
    embed.add_field(name="/hi", value="Say hi to Mr. Swirly!")
    embed.add_field(name="/8ball <question>", value="I will read your future!")
    embed.set_footer(text="This footer doesn't need to be here.")
    await ctx.send(embed=embed)

# /hi
@client.slash_command(name="hi", description="Say hi to Mr. Swirly!")
async def hi(ctx):
    embed = nextcord.Embed(title="Hi!", description="", color=0x9966CB)
    embed.set_footer(text="Use /help for help.")
    await ctx.send(embed=embed)

# /8ball
@client.slash_command(name="8ball", description="I will read your future!")
async def ball(ctx, question):
    answer = random.choice(["Yes.", "No.", "I don't know...", "Kinda.", "Maybe.", "Of course!", "What was the question?", "Nah.", "I don't think so.", "Orange juice.", "Not really.", "Are you sure that's a good question?", "Not a lot.", "Yeah!", "Mmmm...       no."])
    embed = nextcord.Embed(title=answer, description="is your answer.", color=0x9966CB)
    embed.add_field(name="Question:", value=question)
    embed.set_footer(text="Use /help for help.")
    await ctx.send(embed=embed)

# Events
@client.event
async def on_ready():
    print(f"Logging in to discord.com as {client.user.name}")
    embed = nextcord.Embed(title=f"{client.user.name} is online", description="", color=0x9966CB)
    await client.get_channel(1140271893178495076).send(embed=embed)

@client.event
async def on_close():
    print(f"Logging out of discord.com as {client.user.name}")
    embed = nextcord.Embed(title=f"{client.user.name} is offline", description="", color=0x9966CB)
    await client.get_channel(1140271893178495076).send(embed=embed)

# Client Run
client.run(TOKEN)