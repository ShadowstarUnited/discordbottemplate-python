import nextcord
from nextcord.ext import commands
import random
import math

TESTING_GUILD_ID = ServerID # Replace ServerID with your testing server's ServerID

class application(commands.Cog, name='application'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(guild_ids=[TESTING_GUILD_ID], description="This is for testing")
    async def my_slash_command(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("This is a slash command in a cog!")

    @nextcord.user_command(guild_ids=[TESTING_GUILD_ID])
    async def my_user_command(self, interaction: nextcord.Interaction, member: nextcord.Member):
        await interaction.response.send_message(f"Hello, {member}!")

    @nextcord.message_command(guild_ids=[TESTING_GUILD_ID])
    async def my_message_command(self, interaction: nextcord.Interaction, message: nextcord.Message):
        await interaction.response.send_message(f"{message}")
        
def setup(bot):
    bot.add_cog(application(bot))
