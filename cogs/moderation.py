import discord
from discord.ext import commands
import random
import asyncio
import math
from typing import Optional
import sys

class moderation(commands.Cog, name='moderation'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["info"])
    async def userinfo(self, ctx, user:discord.User=None):
        """Gets a user info. Defaults to the user who called the command."""
        if not user:
            user = ctx.author
        em = discord.Embed(title=str(user), description=f"This user joined Discord since {user.created_at.strftime('%b %d, %Y %H:%M:%S')}. In other words this account is {(ctx.message.created_at - user.created_at).days} days old. 👴", color=0x181818)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Nickname", value=user.nick)
        em.add_field(name="Joined At", value=user.joined_at.strftime('%b %d, %Y %H:%M:%S'))
        em.add_field(name="Status", value=f"Chilling in {user.status} mode.")
        em.add_field(name="Tag", value=user.mention)
        em.add_field(name="Roles", value=", ".join([role.name for role in list(reversed(user.roles)) if not role.is_default()]), inline=False)
        await ctx.send(embed=em)
    
    @commands.command()
    @commands.has_guild_permissions(manage_guild=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.User, reason = None):

        if user in ctx.guild.members:
            await ctx.guild.ban(user)
            embed = discord.Embed(description="✅  "+f"Successfully banned **{user}** for reason: {reason}.", color=discord.Color.orange())
            await ctx.reply(embed=embed, mention_author=False)

        else:
            await ctx.guild.ban(user)
            embed = discord.Embed(description="✅  "+f"Successfully banned **{user}** for reason: {reason}.", color=discord.Color.orange())
            await ctx.reply(embed=embed, mention_author=False)
    
    @ban.error    
    async def ban_error(self, ctx, error):    
        if isinstance(error, commands.BadArgument):
            await ctx.reply("User not found. Please make sure the UserID is correct.", mention_author=False, allowed_mentions=discord.AllowedMentions(everyone=False))
    
    @commands.command()
    @commands.has_guild_permissions(manage_guild=True)
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int) :
        user = await self.bot.fetch_user(id)
        await ctx.guild.unban(user)
        embed = discord.Embed(description="✅  "+f"Successfully unbanned **{user}**.", color=discord.Color.orange())
        await ctx.reply(embed=embed, mention_author=False)
    
    @unban.error    
    async def unban_error(self, ctx, error):    
        if isinstance(error, commands.BadArgument):
            await ctx.reply("User not found. Please make sure the UserID is correct.", mention_author=False, allowed_mentions=discord.AllowedMentions(everyone=False))


def setup(bot):
    bot.add_cog(moderation(bot))
