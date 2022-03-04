import nextcord
from nextcord import Webhook
from nextcord.ext import commands, tasks
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
        avatar = ctx.author.avatar.url

        if str(ctx.command.name).casefold() in ["roll", "help", "embed", "unban", "ban"]: #basically any time you want to have this error handler ignore a command, just add the name of the command here so you can have a unique handler for each command. These command names are just examples.
            return

        # Error Handlers #
        ## Bot Missing Permissions Error ##
        if isinstance(error, commands.BotMissingPermissions):
            errore = nextcord.Embed(
                title="[ERROR] Bot Missing Permissions",
                description=f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        ## Missing Argument Error ##
        elif isinstance(error, commands.MissingRequiredArgument):
            errore = nextcord.Embed(
                title="[ERROR] Missing Required Argument",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.BadArgument):
            errore = nextcord.Embed(
                title="[ERROR] Bad Argument",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.PrivateMessageOnly):
            errore = nextcord.Embed(
                title="[ERROR] Private Message Command",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.CommandNotFound):
            pass

        elif isinstance(error, commands.NoPrivateMessage):
            errore = nextcord.Embed(
                title="[ERROR] Guild Only Command",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.DisabledCommand):
            errore = nextcord.Embed(
                title="[ERROR] Command Disabled",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.TooManyArguments):
            errore = nextcord.Embed(
                title="[ERROR] Too Many Arguments",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.CommandOnCooldown):
            errore = nextcord.Embed(
                title="[ERROR] Command Cooldown",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            errorom = await ctx.reply(embed=errore)

            await asyncio.sleep(error.retry_after)

            aftercool = nextcord.Embed(
                title="[ERROR] Command Cooldown",
                description=f"{mention}, you can now run `{ctx.command.name}`!",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await errorom.edit(embed=aftercool)

        elif isinstance(error, commands.NotOwner):
            errore = nextcord.Embed(
                title="[ERROR] Owner Only Command",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.MemberNotFound):
            errore = nextcord.Embed(
                title="[ERROR] Member Not Found",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.ChannelNotFound):
            errore = nextcord.Embed(
                title="[ERROR] Channel Not Found",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.ChannelNotReadable):
            errore = nextcord.Embed(
                title="[ERROR] Channel Not Readable",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.RoleNotFound):
            errore = nextcord.Embed(
                title="[ERROR] Role Not Found",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.EmojiNotFound):
            errore = nextcord.Embed(
                title="[ERROR] Emoji Not Found",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.BadBoolArgument):
            errore = nextcord.Embed(
                title="[ERROR] Bad Bool Argument",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.MissingPermissions):
            errore = nextcord.Embed(
                title="[ERROR] Missing Permissions",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.MissingRole):
            errore = nextcord.Embed(
                title="[ERROR] Missing Role",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.BotMissingRole):
            errore = nextcord.Embed(
                title="[ERROR] Bot Missing Role",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.MissingAnyRole):
            errore = nextcord.Embed(
                title="[ERROR] Missing Any Role",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.BotMissingAnyRole):
            errore = nextcord.Embed(
                title="[ERROR] Bot Missing Any Role",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.NSFWChannelRequired):
            errore = nextcord.Embed(
                title="[ERROR] NSFW Channel Required",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.ExtensionError):
            errore = nextcord.Embed(
                title="[ERROR] Extension Error",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

        elif isinstance(error, commands.CheckFailure):
            pass

        else:
            errore = nextcord.Embed(
                title="ERROR",
                description=f"The following Error Occured:\n" +
                f"{error}",
                color=nextcord.Colour.red()
            )
            errore.set_footer(text=time)
            errore.set_author(name=f"{name}#{tag}", icon_url=avatar)
            await ctx.reply(embed=errore)

def setup(bot):
    bot.add_cog(Error(bot))
