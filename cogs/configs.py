from typing import Union

import nextcord
from logzero import logger
from nextcord.ext import commands

from checks import rank
from database import PrefixCol


class Configs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(
        case_insensitive=True,
        description="Display the server prefix or change it to a new one!",
        usage="[optional: set $new_prefix]",
    )
    @rank("blacklist")
    async def prefix(self, ctx: commands.Context):
        if ctx.invoked_subcommand is not None:
            return

        default_perfix = "d!"
        x = await PrefixCol.find_one({"guild": f"{ctx.guild.id}"})

        if x is None:
            prefix = default_perfix

        elif x is not None:
            prefix = x["prefix"]

        embed = nextcord.Embed(
            title="Server Prefix",
            description=f"The prefix is\n\n`{prefix}`",
            color=0x0F60BD,
        )
        await ctx.reply(embed=embed, mention_author=False)

    @prefix.command(name="set")
    @commands.has_guild_permissions(manage_guild=True)
    async def _set(
        self, ctx: commands.Context, *, new_prefix: Union[nextcord.Member, str] = None
    ):
        if isinstance(new_prefix, nextcord.Member):
            return await ctx.send(
                "As funny as it would be to have a user as my prefix, I won't allow it :c"
            )
        if new_prefix is None:
            return await ctx.reply("Please specify a new prefix!", mention_author=False)
        if new_prefix.count("@") and new_prefix != "@":
            return await ctx.reply(
                "Invalid prefix. Try a different prefix that doesn't involve pinging everyone :)",
                mention_author=False,
            )

        default_prefix = "!" # set this to be the default prefix
        x = await PrefixCol.find_one({"guild": f"{ctx.guild.id}"})

        if new_prefix == default_prefix:
            await PrefixCol.delete_one({"guild": f"{ctx.guild.id}"})
        elif new_prefix != default_prefix:
            if x is None:
                await PrefixCol.insert_one(
                    {"guild": f"{ctx.guild.id}", "prefix": f"{new_prefix}"}
                )
            elif x is not None:
                await PrefixCol.update_one(x, {"$set": {"prefix": f"{new_prefix}"}})

        embed = nextcord.Embed(
            title="Server Prefix",
            description=f"Changed the prefix to\n\n`{new_prefix}`",
            color=0x0F60BD,
        )
        await ctx.reply(embed=embed, mention_author=False)

        logger.info(
            '{0} set their custom prefix to "{1}"'.format(ctx.guild.name, new_prefix)
        )


def setup(bot: commands.Bot):
    bot.add_cog(Configs(bot))
# This cog collects custom prefixes
# [prefix]prefix - to display the current server prefix
# [prefix]prefix new [new prefix] - to set a new one
# This also disallows setting a @mention to be a prefix, as funny as that would be. This also includes @everyone and @here
