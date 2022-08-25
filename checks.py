from nextcord.ext import commands
from database import BlacklistCol


def rank(rank: str):
    async def predicate(ctx: commands.Context):
        if rank == 'blacklist':
            x = await BlacklistCol.find_one({'type': 'user', 'id': f'{ctx.author.id}'})
            if x is not None:
                return False
            return True

    return commands.check(predicate)
# This cog checks to see who is blacklisted as soon as the bot boots up
