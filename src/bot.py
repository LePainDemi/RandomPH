# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("RandomPH est lancé !")
   
@client.command()
async def video(ctx):
    

client.run(TOKEN)

