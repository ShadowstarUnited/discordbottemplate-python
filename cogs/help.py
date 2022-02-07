import nextcord
from nextcord.ext import commands
import random
import asyncio
import datetime

class help(commands.Cog, name='help'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["commands"], description="Displays the commands you can use.")
    @commands.guild_only()
    async def help(self, ctx, option=None):
        if option == None:
            page1 = nextcord.Embed (
                title = "__<bot name> Help menu__",
                description = f"To use this help menu, click on the ▶ emoji to advance to the next page, and click ◀ to go back a page! Click ❌ to close the help menu entirely.\n\n```You can type '{ctx.prefix}help [command name]' for more info about a command.```",
                colour = 0x0394fc
            )
            page1.set_thumbnail(url = 'https://i.imgur.com/yVgfgwa.png')
            page1.set_footer(text="footer text")
            page2 = nextcord.Embed (
                title = "**__Commands Page 1__**",
                description = f"This is where you will list your bot's commands.",
                colour = 0x0394fc
            )
            page2.set_footer(text='Page 1')
            page3 = nextcord.Embed (
                title = "**__Commands Page 2__**",
                description = f"This is where you will list more of your bot's commands.",
                colour = 0x0394fc
            )
            page3.set_footer(text='Page 2')
            page4 = nextcord.Embed (
                title = "**__Commands Page 3__**",
                description = f"This is where you will list even more of your bot's commands.",
                colour = 0x0394fc
            )
            page4.set_footer(text='Page 3')
            page5 = nextcord.Embed (
                title = "Page 4",
                description = f"This bot was created and developed by **You#0000**. Please report any issues, or provide feedback to them.",
                colour = 0x0394fc
            )
            page5.set_image(url = 'https://i.imgur.com/yVgfgwa.png')
            page5.set_footer(text='footer text')
        
            pages = [page1, page2, page3, page4, page5]

            message = await ctx.send(embed = page1)
            await message.add_reaction('⏮')
            await message.add_reaction('◀')
            await message.add_reaction('▶')
            await message.add_reaction('⏭')
            await message.add_reaction('❌')

            def check(reaction, user):
                return user == ctx.author

            i = 0
            reaction = None

            while True:
                if str(reaction) == '⏮':
                    i = 0
                    await message.edit(embed = pages[i])
                elif str(reaction) == '◀':
                    if i > 0:
                        i -= 1
                        if i > 0:
                            pages[i].set_footer(text=f'Page {i}')
                        await message.edit(embed = pages[i])
                elif str(reaction) == '▶':
                    if i < len(pages)-1:
                        i += 1
                        if i > 0:
                            if i == len(pages)-1:
                                pages[i].set_footer(text='footer text')
                            else:
                                pages[i].set_footer(text=f'Page {i}')
                        await message.edit(embed = pages[i])
                elif str(reaction) == '⏭':
                    i = len(pages)-1
                    if i > 0:
                        if i == len(pages)-1:
                            pages[i].set_footer(text='footer text')
                        else:
                            pages[i].set_footer(text=f'Page {i}')
                    await message.edit(embed = pages[i])
                elif str(reaction) == '❌':
                    await message.delete()
            
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout = 30.0, check = check)
                    await message.remove_reaction(reaction, user)
                except:
                    break

            try:
                await message.clear_reactions()
            except:
                return

        if option != None:
            command = self.bot.get_command(option)
            cmd = f"{ctx.prefix}{command}"

            if command.description==str(""):
                desc = "No Description"
            else:
                desc = f"{command.description}"

            aliases = command.aliases
            aliases_we_have = ''

            if aliases == None:
                aliases_we_have = 'No Aliases'
            else:
                alias_prep = []
                for alias in aliases:
                    alias_prep.append(f'`{alias}`')
            aliases_we_have += ', '.join(alias_prep)

            if aliases_we_have == '':
                aliases_we_have = "No Aliases"

            if command.signature == None:
                usage = f"{cmd}"
            else:
                usage = f"{cmd} {command.signature}"

            embedCommand = nextcord.Embed(
                colour=0x2f3136,
                title=f"Help • `{cmd}`",
                description=desc
            )

            embedCommand.add_field(name="Usage", value=f"```\n{usage}\n```", inline=False)
            embedCommand.add_field(name="Aliases", value=aliases_we_have, inline=False)


            if command == 'help':
                embedCommand.set_footer(text=f"footer text")

            await ctx.send(embed=embedCommand)

    @help.error
    async def help_error(self, ctx, error):
        botB = ctx.guild.get_member(Your Bot UserID)

        esend = ctx.send

        if isinstance(error, commands.CommandInvokeError):
            eBadArgument = nextcord.Embed(
                colour=0xb3261e,
                title="__Help Error__",
                description=f"**This command doesn't exist.**\nCheck `{ctx.prefix}help` to see what commands are available.",
                timestamp=datetime.datetime.utcnow()
            )

            eBadArgument.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar.url)
            eBadArgument.set_footer(text=f"{botB.name}", icon_url=botB.avatar.url)
            eBadArgument.set_thumbnail(url="https://i.imgur.com/q6u27Ne.png")

            await esend(embed=eBadArgument)

def setup(bot):
    bot.add_cog(help(bot))
