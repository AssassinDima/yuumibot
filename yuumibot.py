import discord
import asyncio
from discord.ext.commands import has_permissions
from discord.ext import commands
import os
import random
import time
import json
from time import sleep
import requests
import shutil
from bs4 import BeautifulSoup
from discord.utils import get
import glob




intents = discord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix="?", intents = intents)
bot.remove_command("help")



@bot.event
async def on_ready():
    print("DIMA'S BOT ONLINE")


@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)




@bot.command(pass_context=True)
async def pic(ctx, *, arg):
    arg=str(arg)
    files=(glob.glob("*"))
    if arg in files:
        await ctx.send(file=discord.File(arg))
    else :
        await ctx.send("The name of the picture was not here.")

token = open(f"token.txt", "r")

bot.run(token.read())
