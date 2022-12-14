#!/usr/bin/python3

import disnake
from disnake.ext import commands

prefix = '!'
intents = disnake.Intents.all()
bot = commands.Bot(
    command_prefix = commands.when_mentioned_or(prefix),
    help_command = None,
    intents = intents
)

with open("TOKEN.txt", 'r') as file:
    TOKEN = file.read()



######################
##### BOT EVENTS #####
######################



@bot.event
async def on_ready():
    print("Bot connected.")



######################
#### BOT COMMANDS ####
######################


@bot.command()
async def ping(ctx):
    await ctx.send("Pong")


######################



bot.run(TOKEN)
