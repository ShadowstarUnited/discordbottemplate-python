import nextcord
from nextcord.ext import commands


class logs(commands.Cog, name="logs"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: nextcord.Guild):
        embed = nextcord.Embed(title=f"Joined Guild: {guild.name}", color=0x7EEBEB)
        embed.add_field(
            name="Name/ID", value=f"{guild.name} (`{guild.id}`)", inline=True
        )
        embed.add_field(
            name="Server Owner",
            value=f"{guild.owner} (`{guild.owner.id}`)",
            inline=True,
        )
        embed.add_field(
            name="Server Created On", value=f"{guild.created_at} UTC", inline=True
        )
        embed.add_field(name="Member Count", value=f"{guild.member_count}", inline=True)
        embed.set_thumbnail(url=guild.icon)
        logs = self.bot.get_channel(000000000000) #Channel ID
        await logs.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: nextcord.Guild):
        embed = nextcord.Embed(title=f"Left Guild: {guild.name}", color=0x7EEBEB)
        embed.add_field(
            name="Name/ID", value=f"{guild.name} (`{guild.id}`)", inline=True
        )
        embed.add_field(
            name="Server Owner",
            value=f"{guild.owner} (`{guild.owner.id}`)",
            inline=True,
        )
        embed.add_field(
            name="Server Created On", value=f"{guild.created_at} UTC", inline=True
        )
        embed.add_field(name="Member Count", value=f"{guild.member_count}", inline=True)
        embed.set_thumbnail(url=guild.icon)
        logs = self.bot.get_channel(000000000000) #Channel ID
        await logs.send(embed=embed)


def setup(bot):
    bot.add_cog(logs(bot))
# This is where your bot will log when it joins or leaves a server.
