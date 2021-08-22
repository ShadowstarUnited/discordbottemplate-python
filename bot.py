import discord
import os
from discord.ext import commands
import random
import traceback
import sys
from discord.ext import tasks
from itertools import cycle

bot = commands.AutoShardedBot(command_prefix=['bot prefix'], help_command=None, case_insensitive=True, owner_ids=[your user id])
bot.remove_command('help')

path = os.getcwd()
directory = f'{path}/cogs/'
files_in_directory = os.listdir(directory)

cogs = [f'cogs.{file[:-3]}' for file in files_in_directory if file.endswith(".py")]
@bot.event
async def on_ready():

    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    bot.load_extension("jishaku")
    for cog in cogs:
        bot.load_extension(cog)
    print(f'\nLogged in as: {bot.user.name}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{members} members"))

bot.run('bot token')
