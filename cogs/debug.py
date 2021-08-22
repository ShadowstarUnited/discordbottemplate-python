import discord
from discord.ext import commands
import random
import asyncio
import math
from typing import Optional
import sys

class debug(commands.Cog, name='debug'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["botping", "latency"], description="Checks the bot's latency.")
    async def ping(self, ctx):
        ping = math.floor(self.bot.latency * 1000)
        await ctx.send(f"My latency is **{ping}**ms.")

    @commands.command(description="Sends the bot's invitation link.")
    async def invite(self, ctx):
        await ctx.send(f"You can invite me here: <Paste your OAuth2 Link here>")

    @commands.command(description="Sends a Discord Server Invite to the bot's Support Server.")
    async def support(self, ctx):
        await ctx.send(f"You can join my support server here: <Paste your discord.gg link here>")

    @commands.command(description="Displays our Privacy Policy.")
    async def privacy(self, ctx):
        await ctx.send("<Paste your privacy policy here>")

    @commands.command(description='Displays detailed info about the bot')
    async def botinfo(self, ctx):
        calc = discord.Embed(description="Gathering Information... Please wait.")
        msg = await ctx.send(embed=calc)

        # Ping #
        mping = int((msg.created_at - ctx.message.created_at).total_seconds() * 1000)
        wsping = round(self.bot.latency * 1000)

        # Info #
        guilds = len(self.bot.guilds)
        users = len(self.bot.users)

        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1

        system = f"Library: Discord.Py Version {discord.__version__}\n Language: Python Version {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}\nOperating System: {sys.platform}"

        done = discord.Embed(
            title="{} Information".format(self.bot.user),
            description=f"<Put the description of your bot here>",
            color=0x0f60bd
        )
        done.add_field(name="System Info", value=system)
        done.add_field(name="Ping:", value=f"Message Edit: {mping}ms\nBot Latency: {wsping}ms")
        done.add_field(name="Guild Count:", value=guilds)
        done.add_field(name="User Count:", value=members)
        done.set_thumbnail(url = 'bot profile picture image link')
        done.set_footer(text='<Put footer text here, example would be bot version and date>')
        await msg.edit(embed=done)

def setup(bot):
    bot.add_cog(debug(bot))
