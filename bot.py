from typing import Optional
import nextcord
import tokens
import os
from nextcord.ext import commands, tasks
from itertools import cycle
from database import PrefixCol

intents=nextcord.Intents.all()


async def get_prefix(bot: commands.Bot, message: nextcord.Message):
    guild: Optional[nextcord.Guild] = message.guild
    if guild is None:
        return
    x = await PrefixCol.find_one({"guild": f"{guild.id}"})
    if x is None:
        return commands.when_mentioned_or("d!")(bot, message)
    elif x is not None:
        custom_prefix = x["prefix"]
        return commands.when_mentioned_or(custom_prefix)(bot, message)


bot = commands.AutoShardedBot(
    case_insensitive=True, intents=intents, command_prefix=get_prefix
)
bot.remove_command("help")
bot.owner_ids = [
    000000000000000000,
]  # Your Discord UserID. You can put multiple UserID's, but make sure they're on a separate line, with a , at the end.

path = os.getcwd()
directory = f"{path}/cogs/"
files_in_directory = os.listdir(directory)
cogs = [f"cogs.{file[:-3]}" for file in files_in_directory if file.endswith(".py")]

bot.load_extension("jishaku")
for cog in cogs:
    bot.load_extension(cog)


@bot.event
async def on_ready():
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1
    print(f'\nLogged in as: {bot.user.name}')
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name=f"{members} members"))


if __name__ == "__main__":
    bot.run(tokens.bot)
