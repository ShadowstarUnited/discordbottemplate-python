import discord
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands, tasks
import datetime
import os
import json
import asyncio
import requests
import random
import aiohttp

class Error(commands.Cog):
    """The Cog that handles Errors"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Error Handing"""

        # Variables #
        ## Time Stuff ##
        timezone = datetime.timezone(offset=datetime.timedelta(hours=-4), name="EDT")
        now = datetime.datetime.now(tz=timezone)
        time = now.strftime("%x | %X")

        ## Error Stuff ##
        guild = ctx.guild

        ## Member Stuff ##
        author = ctx.author
        name = ctx.author.display_name
        tag = ctx.author.discriminator
        mention = ctx.author.mention
        uid = ctx.author.id
        avatar = ctx.author.avatar_url

        url = "webhook link for logging errors in a discord channel"

        if str(ctx.command.name).casefold() in ["roll", "help", "embed", "unban", "ban"]: #any commands you don't want the error handler to notice
            return

        async with aiohttp.ClientSession() as session:
            logs = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
            embed = discord.Embed(
                title="New Error",
                color=discord.Colour.red()
            )
            if isinstance(ctx.channel, discord.TextChannel):
                embed.add_field(name="Guild", value=ctx.guild, inline=False)
            embed.add_field(name="Channel", value=ctx.channel, inline=False)
            embed.add_field(name="Author", value="{0} (`{0.id}`)".format(author), inline=False)
            embed.add_field(name="Message Content", value=ctx.message.content, inline=False)
            embed.add_field(name="Error", value=error, inline=False)
            await logs.send(embed=embed)

        # Error Handlers #
        ## Bot Missing Permissions Error ##
        if isinstance(error, commands.BotMissingPermissions):
            errore = discord.Embed(
                title="[ERROR] Bot Missing Permissions",
                description=f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        ## Missing Argument Error ##
        elif isinstance(error, commands.MissingRequiredArgument):
            errore = discord.Embed(
                title="[ERROR] Missing Required Argument",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.BadArgument):
            errore = discord.Embed(
                title="[ERROR] Bad Argument",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.PrivateMessageOnly):
            errore = discord.Embed(
                title="[ERROR] Private Message Command",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.CommandNotFound):
            pass

        elif isinstance(error, commands.NoPrivateMessage):
            errore = discord.Embed(
                title="[ERROR] Guild Only Command",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.DisabledCommand):
            errore = discord.Embed(
                title="[ERROR] Command Disabled",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.TooManyArguments):
            errore = discord.Embed(
                title="[ERROR] Too Many Arguments",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.CommandOnCooldown):
            errore = discord.Embed(
                title="[ERROR] Command Cooldown",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            errorom = await ctx.reply(embed=errore)

            await asyncio.sleep(error.retry_after)

            aftercool = discord.Embed(
                title="[ERROR] Command Cooldown",
                description=f"{mention}, you can now run `{ctx.command.name}`!",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await errorom.edit(embed=aftercool)

        elif isinstance(error, commands.NotOwner):
            errore = discord.Embed(
                title="[ERROR] Owner Only Command",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.MemberNotFound):
            errore = discord.Embed(
                title="[ERROR] Member Not Found",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.ChannelNotFound):
            errore = discord.Embed(
                title="[ERROR] Channel Not Found",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.ChannelNotReadable):
            errore = discord.Embed(
                title="[ERROR] Channel Not Readable",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.RoleNotFound):
            errore = discord.Embed(
                title="[ERROR] Role Not Found",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.EmojiNotFound):
            errore = discord.Embed(
                title="[ERROR] Emoji Not Found",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.BadBoolArgument):
            errore = discord.Embed(
                title="[ERROR] Bad Bool Argument",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.MissingPermissions):
            errore = discord.Embed(
                title="[ERROR] Missing Permissions",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.MissingRole):
            errore = discord.Embed(
                title="[ERROR] Missing Role",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.BotMissingRole):
            errore = discord.Embed(
                title="[ERROR] Bot Missing Role",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.MissingAnyRole):
            errore = discord.Embed(
                title="[ERROR] Missing Any Role",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.BotMissingAnyRole):
            errore = discord.Embed(
                title="[ERROR] Bot Missing Any Role",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.NSFWChannelRequired):
            errore = discord.Embed(
                title="[ERROR] NSFW Channel Required",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.ExtensionError):
            errore = discord.Embed(
                title="[ERROR] Extension Error",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.CheckFailure):
            pass

        else:
            errore = discord.Embed(
                title="ERROR",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=discord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

def setup(bot):
    bot.add_cog(Error(bot))
