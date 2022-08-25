import nextcord
from nextcord.ext import commands, menus

from checks import rank
from database import PrefixCol


class help(commands.Cog, name="help"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(
        aliases=["commands"],
        description="Displays the commands you can use. You can also display advanced info when you use it with a command after it!",
    )
    @rank("blacklist")
    @commands.guild_only()
    async def help(self, ctx: commands.Context, option: str = None):
        x = await PrefixCol.find_one({"guild": f"{ctx.guild.id}"})

        if x is None:
            prefix = "!" # change to whatever prefix your bot uses

        elif x is not None:
            prefix = x["prefix"]

        if option is None:
            page1 = nextcord.Embed(
                title="__<bot name> Help menu__", #change <bot name> to your bot's name
                description=f"""
This help menu uses the new buttons system.
To use this help menu, click on the ➡️ button to advance to the next page, and click ⬅️ to go back a page! Click ⏹️ to disable button feedback.
```You can type '{prefix}help [command name]' for more info about a command.```
                """,
                colour=0x0394FC,
            )
            page1.set_thumbnail(url="https://i.imgur.com/yVgfgwa.png")
            page1.set_footer(text="Page 1/6")

            page2 = nextcord.Embed(
                title="**__Page 1__**",
                description=f"""
You can put some commands in here.
                """,
                colour=0x0394FC,
            )
            page2.set_footer(text="Page 2/6")

            page3 = nextcord.Embed(
                title="**__Page 2__**",
                description=f"""
You can put more commands in here.
                """,
                colour=0x0394FC,
            )
            page3.set_footer(text="Page 3/6")

            page4 = nextcord.Embed(
                title="**__Page 3__**",
                description=f"""
The amount of commands you can put here are endless!
                """,
                colour=0x0394FC,
            )
            page4.set_footer(text="Page 4/6")

            page5 = nextcord.Embed(
                title="**__Page 4__**",
                description=f"""
Seriously? You need 4 PAGES of commands?!?!
                """,
                colour=0x0394FC,
            )
            page5.set_footer(text="Page 5/6")

            page6 = nextcord.Embed(
                title="Information",
                description="This bot was created and developed by **Username#0000**. Please report any issues, or provide feedback to them.",
                colour=0x0394FC,
            )
            page6.set_image(url="https://i.imgur.com/74rlP4b.gif")
            page6.set_footer(text="Page 6/6")

            pages = [page1, page2, page3, page4, page5, page6]

            await HelpMenu(ctx, pages).start(ctx)

        if option is not None:
            command = self.bot.get_command(option)
            if command is None:
                return await ctx.reply(
                    f"That command does not exist. Make sure you typed it correctly, or type `{prefix}help` for a full list of usable commands.",
                    mention_author=False,
                )
            cmd = f"{prefix}{command}"

            if command.description == str(""):
                desc = "No Description"
            else:
                desc = f"{command.description}"

            aliases = command.aliases
            aliases_we_have = ""

            if aliases is None:
                aliases_we_have = "No Aliases"
            else:
                alias_prep = []
                for alias in aliases:
                    alias_prep.append(f"`{alias}`")
            aliases_we_have += ", ".join(alias_prep)

            if aliases_we_have == "":
                aliases_we_have = "No Aliases"

            if command.signature is None:
                usage = f"{cmd}"
            else:
                usage = f"{cmd} {command.signature}"

            embedCommand = nextcord.Embed(
                colour=0x2F3136, title=f"Help • `{cmd}`", description=desc
            )

            embedCommand.add_field(
                name="Usage", value=f"```\n{usage}\n```", inline=False
            )
            embedCommand.add_field(name="Aliases", value=aliases_we_have, inline=False)

            # user = ctx.guild.get_member(830446905611517982)

            if command == "help":
                embedCommand.set_footer(text="Page 5/5")

            await ctx.send(embed=embedCommand)


class HelpMenu(menus.ButtonMenu):
    def __init__(self, ctx, pages=[]):
        super().__init__(disable_buttons_after=True, timeout=60.0)
        self.pages = pages
        self.ctx = ctx

    async def send_initial_message(self, channel, ctx):
        self.prefix = self.ctx.prefix
        self.currentPage = 0
        self.lastPage = len(self.pages) - 1
        return await channel.send(embed=self.pages[self.currentPage], view=self)

    @nextcord.ui.button(emoji="⏮")
    async def on_first(self, button, interaction):
        if self.ctx.author != interaction.user:
            await interaction.response.send_message(
                "This interaction is not for you.", ephemeral=True
            )
            return
        self.currentPage = 0
        await self.message.edit(embed=self.pages[self.currentPage])

    @nextcord.ui.button(emoji="⬅️")
    async def on_previous(self, button, interaction):
        if self.ctx.author != interaction.user:
            await interaction.response.send_message(
                "This interaction is not for you.", ephemeral=True
            )
            return
        if self.currentPage - 1 != -1:
            self.currentPage -= 1
            await self.message.edit(embed=self.pages[self.currentPage])

    @nextcord.ui.button(emoji="⏹")
    async def on_stop(self, button, interaction):
        if self.ctx.author != interaction.user:
            await interaction.response.send_message(
                "This interaction is not for you.", ephemeral=True
            )
            return
        self.stop()

    @nextcord.ui.button(emoji="➡️")
    async def on_next(self, button, interaction):
        if self.ctx.author != interaction.user:
            await interaction.response.send_message(
                "This interaction is not for you.", ephemeral=True
            )
            return
        if self.currentPage + 1 != len(self.pages):
            self.currentPage += 1
            await self.message.edit(embed=self.pages[self.currentPage])

    @nextcord.ui.button(emoji="⏭")
    async def on_last(self, button, interaction):
        if self.ctx.author != interaction.user:
            await interaction.response.send_message(
                "This interaction is not for you.", ephemeral=True
            )
            return
        self.currentPage = self.lastPage
        await self.message.edit(embed=self.pages[self.currentPage])


def setup(bot):
    bot.add_cog(help(bot))
