import asyncio
import importlib
import datetime
import os
from subprocess import Popen
import subprocess

from nextcord.ext import commands
from nextcord import utils

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot:commands.Bot = bot

    async def cog_check(self, ctx):
        return await ctx.bot.is_owner(ctx.author)

    @commands.command(hidden=True, description='Admin only command. Reloads a cog. .reload [cogname]')
    async def reload(self, ctx, *, cog: str):
        cogs = []
        for c in ctx.bot.cogs:
            cogs.append(c.replace('Cog', ''))

        if cog in cogs:
            self.bot.unload_extension(f"cogs.{cog}")
            self.bot.load_extension(f"cogs.{cog}")
            await ctx.send(f'Successfully reloaded the **{cog}** cog.')
        else:
            await ctx.send(f"Cog does not exist.")

def setup(bot):
    bot.add_cog(Reload(bot))
