from datetime import datetime

import nextcord
from logzero import logger
from nextcord.ext import commands

from database import BlacklistCol, UserCol
from functions import find_user


class Blacklist(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener("on_ready")
    async def ready_launch(self):
        for guild in self.bot.guilds:
            doc = await BlacklistCol.find_one({"type": "guild", "id": str(guild.id)})
            if doc:
                await guild.leave()

    @commands.group()
    @commands.is_owner()
    async def blacklist(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid add command passed...")

    @blacklist.command(name="view", aliases=["check"])
    async def _view(self, ctx: commands.Context, type: str, *, value: int):
        if type == "user":
            doc = await BlacklistCol.find_one({"type": "user", "id": f"{value}"})

            if doc is None:
                embed = nextcord.Embed(
                    title="User Not in Blacklist!", color=nextcord.Colour.red()
                )
                await ctx.reply(embed=embed, mention_author=False)

            elif doc is not None:
                user = await self.bot.fetch_user(value)

                embed = nextcord.Embed(
                    title="Blacklisted User:",
                    description=f"**Username#Tag**: {user}\n**User ID**: {user.id}\n**Reason**: {doc['reason']}",
                    color=0x0F60BD,
                )
                await ctx.reply(embed=embed, mention_author=False)

        elif type == "guild":
            doc = await BlacklistCol.find_one({"type": "guild", "id": f"{value}"})

            if doc is None:
                embed = nextcord.Embed(
                    title="Guild Not in Blacklist!", color=nextcord.Colour.red()
                )
                await ctx.reply(embed=embed, mention_author=False)

            elif doc is not None:
                embed = nextcord.Embed(
                    title="Blacklisted Guild:",
                    description=f"**Guild ID**: {value}\n**Reason**: {doc['reason']}",
                    color=0x0F60BD,
                )
                await ctx.reply(embed=embed, mention_author=False)

    @blacklist.command(name="guild", aliases=["server"])
    async def _guild(self, ctx: commands.Context, guildid: int, *, reason: str):
        """blacklists ID provided"""
        guild = self.bot.get_guild(guildid)
        prefix = ctx.prefix

        if reason:
            reason = reason
        else:
            reason = "No Reason Specified"

        doc = await BlacklistCol.find_one({"id": guildid})
        if doc is None:
            await BlacklistCol.insert_one(
                {"type": "guild", "id": f"{guildid}", "reason": f"{reason}"}
            )

            if guild:
                now = datetime.now()
                time = now.strftime("%A, %B %d, %Y %H:%M (GMT)")
                await guild.leave()
                content = "I have left **{}** successfully!".format(guild.name)
                added_embed = nextcord.Embed(
                    title="Successfully added **{0}** to the Server Blacklist!".format(
                        guild.name
                    ),
                    description=f"Guild Name: {guild.name}\n" + f"Reason: {reason}",
                    color=0x0F60BD,
                )
                added_embed.set_footer(text=time)
                await ctx.send(content=content, embed=added_embed)

            if not guild:
                now = datetime.now()
                time = now.strftime("%A, %B %d, %Y %H:%M (GMT)")
                added_embed = nextcord.Embed(
                    title="Successfully added **{0}** to the Server Blacklist!".format(
                        guildid
                    ),
                    description=f"Reason: {reason}",
                    color=0x0F60BD,
                )
                added_embed.set_footer(text=time)
                await ctx.send(embed=added_embed)

            logger.info("Added Server {} to the blacklist!".format(guildid))

        if doc is not None:
            if guild:
                errore = nextcord.Embed(
                    title="Guild Already Blacklisted",
                    description=f"{guild.name} (`{guildid}`) is already blacklisted! To whitelist the guild, run `{prefix}whitelist guild <guildID>`!",
                    color=nextcord.Colour.red(),
                )
                await ctx.send(embed=errore)
                await guild.leave()
                leave_message = "I have left **{}** successfully!".format(guild.name)
                await ctx.send(leave_message)

            if not guild:
                errore = nextcord.Embed(
                    title="Guild Already Blacklisted",
                    description=f"`{guildid}` is already blacklisted! To whitelist the guild, run `{prefix}whitelist guild <guildID>`!",
                    color=nextcord.Colour.red(),
                )
                await ctx.send(embed=errore)

    @blacklist.command(name="user", aliases=["member"])
    async def _user(self, ctx: commands.Context, memberid: int, *, reason):
        """blacklists ID provided"""
        user = await self.bot.fetch_user(memberid)
        prefix = ctx.prefix

        if reason:
            reason = reason
        else:
            reason = "No Reason Specified"

        doc = await BlacklistCol.find_one({"type": "user", "id": f"{memberid}"})
        if doc is None:
            await BlacklistCol.insert_one(
                {"type": "user", "id": f"{memberid}", "reason": f"{reason}"}
            )

            userdb = await find_user(memberid)
            if userdb is not None:
                await UserCol.delete_one({"_id": memberid})

            now = datetime.now()
            time = now.strftime("%A, %B %d, %Y %H:%M (GMT)")
            added_embed = nextcord.Embed(
                title="Successfully added **{0}** (`{0.id}`) to the User Blacklist!".format(
                    user
                ),
                description=f"Reason: {reason}",
                color=0x0F60BD,
            )
            added_embed.set_footer(text=time)
            await ctx.send(embed=added_embed)

            logger.info("Added User {} to the blacklist!".format(memberid))

        if doc is not None:
            errore = nextcord.Embed(
                title="User Already Blacklisted",
                description=f"{user.name} (`{memberid}`) is already blacklisted! To whitelist the user, run `{prefix}whitelist user <memberID>`!",
                color=nextcord.Colour.red(),
            )
            await ctx.send(embed=errore)

    @commands.group()
    @commands.is_owner()
    async def whitelist(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            await ctx.send("Invalid add command passed...")

    @whitelist.command(name="guild", aliases=["server"])
    async def guild(self, ctx: commands.Context, guildid: int):
        """removes from blacklist ID provided"""
        prefix = ctx.prefix

        doc = await BlacklistCol.find_one({"id": f"{guildid}"})

        if doc is None:
            errore = nextcord.Embed(
                title="Guild is not Blacklisted",
                description=f"`{guildid}` is not blacklisted! To blacklist the guild, run `{prefix}blacklist guild <guildID>`!",
                color=nextcord.Colour.red(),
            )
            await ctx.send(embed=errore)

        elif doc is not None:
            await BlacklistCol.delete_one({"id": f"{guildid}"})
            now = datetime.now()
            time = now.strftime("%A, %B %d, %Y %H:%M (GMT)")
            added_embed = nextcord.Embed(
                description="Successfully removed **{0}** from the Server Blacklist!".format(
                    guildid
                ),
                color=0x0F60BD,
            )
            added_embed.set_footer(text=time)
            await ctx.send(embed=added_embed)
            logger.info(
                "Successfully removed **{0}** from the Server Blacklist!".format(
                    guildid
                )
            )

    @whitelist.command(name="user", aliases=["member"])
    async def user(self, ctx: commands.Context, memberid: int):
        """removes from blacklist ID provided"""

        user = await self.bot.fetch_user(memberid)
        prefix = ctx.prefix

        doc = await BlacklistCol.find_one({"id": f"{memberid}"})

        if doc is None:
            errore = nextcord.Embed(
                title="User is not Blacklisted",
                description="{0} (`{1}`) is not blacklisted! To blacklist the user, run `{2}blacklist user <memberID>`!".format(
                    user.name, memberid, prefix
                ),
                color=nextcord.Colour.red(),
            )
            await ctx.send(embed=errore)

        elif doc is not None:
            await BlacklistCol.delete_one({"id": f"{memberid}"})
            now = datetime.now()
            time = now.strftime("%A, %B %d, %Y %H:%M (GMT)")
            added_embed = nextcord.Embed(
                description="Successfully removed **{0}** (`{1}`) from the User Blacklist!".format(
                    user.name, memberid
                ),
                color=0x0F60BD,
            )
            added_embed.set_footer(text=time)
            await ctx.send(embed=added_embed)
            logger.info(
                "Successfully removed **{0}** (`{1}`) from the User Blacklist!".format(
                    user.name, memberid
                )
            )


def setup(bot: commands.Bot):
    bot.add_cog(Blacklist(bot))
# This cog is the entire code for the blacklist system, including the commands.
# [prefix]blacklist user <userid> <reason> or [prefix]blacklist guild <serverid> <reason>
# And [prefix]whitelist user <userid> or [prefix]whitelist guild <serverid>
# And [prefix]blacklist view user/guild <userid/serverid>
