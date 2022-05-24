import disnake, asyncio
from disnake.ext import commands

prefix = '!'
intents = disnake.Intents.all()
bot = commands.Bot(
    command_prefix = commands.when_mentioned_or(prefix),
    help_command = None,
    intents = intents
)

TOKEN = ""


######################
##### BOT EVENTS #####
######################





######################
#### BOT COMMANDS ####
######################




######################


bot.run(TOKEN)
