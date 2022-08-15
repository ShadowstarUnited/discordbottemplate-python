import nextcord
import os
from nextcord.ext import commands
import random
import traceback
from nextcord.ext import tasks
from itertools import cycle

bot = commands.AutoShardedBot(command_prefix=['!'], intents=nextcord.Intents.all(), help_command=None, case_insensitive=True, owner_ids=[Your UserID]) #Paste your Discord UserID here
bot.remove_command('help') #removes the built in help command to allow the custom paginated one to work

path = os.getcwd()
directory = f'{path}/cogs/'
files_in_directory = os.listdir(directory)
cogs = [f'cogs.{file[:-3]}' for file in files_in_directory if file.endswith(".py")]

bot.load_extension('jishaku')
for cog in cogs:
    bot.load_extension(cog)
    
@bot.event
async def on_ready():
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1
    print(f'\nLogged in as: {bot.user.name}')
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"{members} members"))

bot.run('Your Bot Token')
