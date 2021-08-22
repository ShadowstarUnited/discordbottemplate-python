import discord
from discord.ext import commands
import random
import asyncio
import math
from typing import Optional
import sys

class Owner(commands.Cog, name='owner'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Sends a message to the designated channel.", usage="[channel] <message>")
    @commands.is_owner()
    async def echo(self, ctx, channel: Optional[discord.TextChannel], *, content: str):
        channel = channel or ctx.channel
        await ctx.message.delete()
        await channel.send(content, allowed_mentions=discord.AllowedMentions(everyone=False))

    @commands.command(aliases=['makeinvite'], description="A developer only command that creates an invite to a server when a Guild ID is provided.")
    @commands.is_owner()
    async def createinvite(self, ctx, ID : int):
        guild = self.bot.get_guild(ID)
        try:
            invite = (await guild.invites())[0]
        except (IndexError, discord.Forbidden):
            try:
                invite = await guild.text_channels[0].create_invite(max_age=120)
            except discord.Forbidden:
                return await ctx.send("Unable to create invite")
        return await ctx.send(f"Here is the invite: https://discord.gg/{invite.code}")

    @commands.command(aliases=['lookup'], description="Finds a server with a given name.")
    @commands.is_owner()
    async def findserver(self, ctx, name):
        guilds = []
        [guilds.append(guild) for guild in self.bot.guilds if guild.name.casefold().count(name.casefold()) > 0]
        guilds = [f"{guild.name} `{guild.id}` ({guild.member_count} members)" for guild in guilds]

        await self._send_guilds(ctx, guilds, "Servers Found")

    @commands.command(description="A developer only command that makes the bot leave the given server when a Guild ID is provided.")
    @commands.is_owner()
    async def leaveserver(self, ctx, ID : int):
        guild = await self.bot.fetch_guild(ID)
        owner = await self.bot.fetch_user(guild.owner_id)
        if not guild:
            return await ctx.send("Invalid Guild ID")
        else:
            one = '1️⃣'
            two = '2️⃣'
            three = '3️⃣'
            four = '4️⃣'
            five = '5️⃣'
            six = '6️⃣'
            seven = '7️⃣'

            def react_check(reaction, user):
                if user.id not in self.bot.owner_ids:
                    return False
                elif user.id in self.bot.owner_ids:
                    if user == ctx.author:
                        if str(reaction.emoji) == one:
                            return True
                        elif str(reaction.emoji) == two:
                            return True
                        elif str(reaction.emoji) == three:
                            return True
                        elif str(reaction.emoji) == four:
                            return True
                        elif str(reaction.emoji) == five:
                            return True
                        elif str(reaction.emoji) == six:
                            return True
                        elif str(reaction.emoji) == seven:
                            return True
                        else:
                            return False
                    else:
                        return False

            def msg_check(m):
                if m.author.id not in self.bot.owner_ids:
                    return False
                elif m.author.id in self.bot.owner_ids:
                    if m.author == ctx.author and m.channel == ctx.channel:
                        return True

            reasons = f"1. Your server violates Discord's Terms of Service, or includes content that does.\n2. You or your server's members were spamming commands which obviously do not exist, filling up our error logging.\n3. You or your server's members were misusing or abusing the bot.\n4. The bot was used to send inappropriate messages via a command sent from you or your admin(s).\n5. The Developer deemed your server unfit for the bot to be in, and felt uncomfortable.\n6. A Discord related issue.\n7. Custom Reason"

            reasonembed = discord.Embed(
              title=f"Reason for Leaving {guild.name}?",
              description=reasons,
              color=discord.Color.blurple()
            )
            botmsg = await ctx.send(embed=reasonembed)
            await botmsg.add_reaction(one)
            await botmsg.add_reaction(two)
            await botmsg.add_reaction(three)
            await botmsg.add_reaction(four)
            await botmsg.add_reaction(five)
            await botmsg.add_reaction(six)
            await botmsg.add_reaction(seven)

            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=react_check, timeout=600.0)

            except Exception as e:
                if isinstance(e, asyncio.TimeoutError):
                    await botmsg.clear_reactions()
                    return await ctx.send("You ran out of time!")

                else:
                    return await ctx.send(content=e)

            else:
                await botmsg.clear_reactions()

                if str(reaction.emoji) == one:
                    reason = f"Your server violates Discord's Terms of Service, or includes content that does."

                    try:
                        owner_embed = discord.Embed(
                            title=f"I left {guild.name}!",
                            description=f"My developer has requested I leave your server: `{guild.name}` for the following reason:\n```{reason}```"
                        )
                        await owner.send(embed=owner_embed)
                    except discord.Forbidden:
                      await ctx.send("I was unable to send a message to that server's owner, however...")
                    await guild.leave()
                    await ctx.send("✅ Successfully left that server!")

                elif str(reaction.emoji) == two:
                    reason = f"You or your server's members were spamming commands which obviously do not exist, filling up our error logging."

                    try:
                        owner_embed = discord.Embed(
                            title=f"I left {guild.name}!",
                            description=f"My developer has requested I leave your server: `{guild.name}` for the following reason:\n```{reason}```"
                        )
                        await owner.send(embed=owner_embed)
                    except discord.Forbidden:
                      await ctx.send("I was unable to send a message to that server's owner, however...")
                    await guild.leave()
                    await ctx.send("✅ Successfully left that server!")

                elif str(reaction.emoji) == three:
                    reason = f"You or your server's members were misusing or abusing the bot."

                    try:
                        owner_embed = discord.Embed(
                            title=f"I left {guild.name}!",
                            description=f"My developer has requested I leave your server: `{guild.name}` for the following reason:\n```{reason}```"
                        )
                        await owner.send(embed=owner_embed)
                    except discord.Forbidden:
                      await ctx.send("I was unable to send a message to that server's owner, however...")
                    await guild.leave()
                    await ctx.send("✅ Successfully left that server!")

                elif str(reaction.emoji) == four:
                    reason = f"The bot was used to send inappropriate messages via a command sent from you or your admin(s)."

                    try:
                        owner_embed = discord.Embed(
                            title=f"I left {guild.name}!",
                            description=f"My developer has requested I leave your server: `{guild.name}` for the following reason:\n```{reason}```"
                        )
                        await owner.send(embed=owner_embed)
                    except discord.Forbidden:
                      await ctx.send("I was unable to send a message to that server's owner, however...")
                    await guild.leave()
                    await ctx.send("✅ Successfully left that server!")

                elif str(reaction.emoji) == five:
                    reason = f"The Developer deemed your server unfit for the bot to be in, and felt uncomfortable."

                    try:
                        owner_embed = discord.Embed(
                            title=f"I left {guild.name}!",
                            description=f"My developer has requested I leave your server: `{guild.name}` for the following reason:\n```{reason}```"
                        )
                        await owner.send(embed=owner_embed)
                    except discord.Forbidden:
                      await ctx.send("I was unable to send a message to that server's owner, however...")
                    await guild.leave()
                    await ctx.send("✅ Successfully left that server!")

                elif str(reaction.emoji) == six:
                    reason = f"A Discord related issue."

                    try:
                        owner_embed = discord.Embed(
                            title=f"I left {guild.name}!",
                            description=f"My developer has requested I leave your server: `{guild.name}` for the following reason:\n```{reason}```"
                        )
                        await owner.send(embed=owner_embed)
                    except discord.Forbidden:
                      await ctx.send("I was unable to send a message to that server's owner, however...")
                    await guild.leave()
                    await ctx.send("✅ Successfully left that server!")

                elif str(reaction.emoji) == seven:
                    await ctx.send(f"What is the reason for leaving {guild.name}?")
                    try:
                        reasonm = await self.bot.wait_for('message', check=msg_check, timeout=600.0)

                    except Exception as e:
                        if isinstance(e, asyncio.TimeoutError):
                            await botmsg.clear_reactions()
                            return await ctx.send("You ran out of time!")

                        else:
                            return await ctx.send(content=e)

                    else:
                        reason = reasonm.content
                        await reasonm.delete()

                        try:
                            owner_embed = discord.Embed(
                                title=f"I left {guild.name}!",
                                description=f"My developer has requested I leave your server: `{guild.name}` for the following reason:\n```{reason}```"
                            )
                            await owner.send(embed=owner_embed)
                        except discord.Forbidden:
                          await ctx.send("I was unable to send a message to that server's owner, however...")
                        await guild.leave()
                        await ctx.send("✅ Successfully left that server!")

    async def _send_guilds(self, ctx, guilds, title):
        if len(guilds) == 0:
            await ctx.send(embed=discord.Embed(description="No such guild was found."))
            return

        all_pages = []

        for chunk in [guilds[i : i + 20] for i in range(0, len(guilds), 20)]:
            page = discord.Embed(title=title)

            for guild in chunk:
                if page.description == discord.Embed.Empty:
                    page.description = guild
                else:
                    page.description += f"\n{guild}"

            page.set_footer(text=f"Guilds requested by {ctx.author}")
            all_pages.append(page)

        for page in all_pages:
            await ctx.send(embed=page)
            await asyncio.sleep(2)

    @commands.command(aliases=['serverlist'], description="A developer only command that lists every server the bot is in.")
    @commands.is_owner()
    async def list_guilds(self, ctx):
        servers = self.bot.guilds
        guilds = [f"**{guild.name} - `{guild.id}`**\n{guild.member_count} members\n" for guild in servers]

        await self._send_guilds(ctx, guilds, "Servers I'm In")

    @commands.command(description="Look at server info")
    @commands.is_owner()
    async def infoserver(self, ctx, ID : int):
        guild = self.bot.get_guild(ID)

        if not guild:
            return await ctx.send("I am not a member of that guild!")
        elif guild:
            owner = await self.bot.fetch_user(guild.owner_id)
            # Guild Features #
            features = guild.features

            if guild.features == []:
                feats = "No Guild Features!"

            else:
                featList = [f.replace("_", " ").title() for f in guild.features]

                feats = ', '.join(featList)

            vlevel = f"{guild.verification_level}"
            vlvl = vlevel.title()

            channels = f"Text Channels: {len(guild.text_channels)} | Categories: {len(guild.categories)} | Voice Channels: {len(guild.voice_channels)}"

            embed = discord.Embed(
                title=f"{guild.name} Information",
                color=0x7eebeb
            )
            embed.set_footer(text=f"Guilds requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.add_field(name="Name / ID", value=f"{guild.name} (`{guild.id}`)", inline=True)
            embed.add_field(name="Server Owner", value=f"{owner} (`{owner.id}`)", inline=True)
            embed.add_field(name="Region", value=f"{guild.region}", inline=True)
            embed.add_field(name="Server Created On", value=f"{guild.created_at} UTC", inline=True)
            embed.add_field(name="Boost Tier", value=f"{guild.premium_tier}", inline=True)
            embed.add_field(name="Boost Count", value=f"{guild.premium_subscription_count}", inline=True)
            embed.add_field(name="Member Count", value=f"{guild.member_count}", inline=True)
            embed.add_field(name="Role Count", value=f"{len(guild.roles)}", inline=True)
            embed.add_field(name="Verification Level", value=f"{vlvl}", inline=True)
            embed.add_field(name=f"Channels ({len(guild.channels)})", value=f"{channels}", inline=False)
            embed.add_field(name="Guild Features", value=f"{feats}", inline=False)
            embed.set_thumbnail(url=guild.icon_url)
            ismsg = await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Owner(bot))
