import typing
import inspect
import nextcord
import asyncio
from nextcord.ext import commands
from nextcord.ext.commands.errors import BadColourArgument


class Colours(nextcord.Color):
    @classmethod
    def black(cls):
        return cls(0x000000)

    @classmethod
    def white(cls):
        return cls(0xfafafa)

    @classmethod
    def pink(cls):
        return cls(0xffa3f0)

    @classmethod
    def dark_pink(cls):
        return cls(0x99578e)

    @classmethod
    def yellow(cls):
        return cls(0xeff542)

    @classmethod
    def shadow_purple(cls):
        return cls(0xcc02ff)

    @classmethod
    def silver(cls):
        return cls(0xababab)

    @classmethod
    def lavender(cls):
        return cls(0xb57edc)

    @classmethod
    def light_blue(cls):
        return cls(0xadd8e6)

    @classmethod
    def cyan(cls):
        return cls(0x00ffff)

    @classmethod
    def lime(cls):
        return cls(0x00ff00)

    @classmethod
    def aqua(cls):
        return cls(0x33ffff)

    @classmethod
    def wine_red(cls):
        return cls(0x730d20)

class Converter(commands.Converter):
    async def convert(self, ctx, argument):
        arg = argument.replace('0x', '').lower()
        if arg[0] == '#':
            arg = arg[1:]
        try:
            value = int(arg, base=16)
            if not (0 <= value <= 0xFFFFFF):
                raise BadColourArgument(arg)
            return Colours(value=value)
        except ValueError:
            arg = arg.replace(' ', '_')
            method = getattr(Colours, arg, None)
            if arg.startswith('from_') or method is None or not inspect.ismethod(method):
                raise BadColourArgument(arg)
            return method()

class sendembed(commands.Cog, name='sendembed'):
    def __init__(self, bot):
        self.bot = bot

    @commands.bot_has_permissions(embed_links=True)
    @commands.has_guild_permissions(manage_guild=True)
    @commands.command(name="embed", aliases=["sendembed"], description="Sends an embedded message. You do not need to specify a channel or color, but you can if you want to! You can type the name of a color or use a hex color code, but make sure it has an 0x before the hex. You can even have it send an image; simply attach the image with the message. Check out the usage below.")
    async def embed(self, ctx: commands.Context, channel: typing.Optional[nextcord.TextChannel], color: typing.Optional[Converter], *, text: str = None):

        def m_check(m):
            if m.author == ctx.author and m.channel == ctx.channel:
                return True
            else:
                return False

        if not channel:
            channel = ctx.channel
        if not color:
            color = Colours.orange()
        if not text:
            embed1 = nextcord.Embed(
                title="Interactive Embed Setup",
                description=f"What is the title of the embed?\nTo have an empty title, reply with `skip`!",
                color=Colours.silver()
            )
            embed1.set_footer(text="You have 2 minutes to respond!")
            botmsg = await ctx.send(embed=embed1)

            try:
                um1 = await self.bot.wait_for('message', check=m_check, timeout=120.0)

            except Exception as e:
                if isinstance(e, asyncio.TimeoutError):
                    error = nextcord.Embed(
                        description=f"Embed Setup Cancelled! You didn't reply in time!",
                        color=Colours.wine_red()
                    )
                    await botmsg.edit(embed=error)

                else:
                    await ctx.send(e)

            else:
                if um1.content.lower() == 'skip':
                    title_content = None
                elif um1.content.lower() != 'skip':
                    title_content = um1.content
                await um1.delete()

                embed2 = nextcord.Embed(
                    title="Interactive Embed Setup",
                    description=f"What is the description of the embed?\nTo have an empty description, reply with `skip`!",
                    color=Colours.silver()
                )
                embed1.set_footer(text="You have 2 minutes to respond!")
                await botmsg.edit(embed=embed2)

                try:
                    um2 = await self.bot.wait_for('message', check=m_check, timeout=120.0)

                except Exception as e:
                    if isinstance(e, asyncio.TimeoutError):
                        error = nextcord.Embed(
                            description=f"Embed Setup Cancelled! You didn't reply in time!",
                            color=Colours.wine_red()
                        )
                        await botmsg.edit(embed=error)

                    else:
                        await ctx.send(e)

                else:
                    if um2.content.lower() == 'skip':
                        desc_content = None
                    elif um2.content.lower() != 'skip':
                        desc_content = um2.content
                    await um2.delete()

                    embed3 = nextcord.Embed(
                        title="Interactive Embed Setup",
                        description=f"What is the footer of the embed?\nTo have an empty footer, reply with `skip`!",
                        color=Colours.silver()
                    )
                    embed1.set_footer(text="You have 2 minutes to respond!")
                    await botmsg.edit(embed=embed3)

                    try:
                        um3 = await self.bot.wait_for('message', check=m_check, timeout=120.0)

                    except Exception as e:
                        if isinstance(e, asyncio.TimeoutError):
                            error = nextcord.Embed(
                                description=f"Embed Setup Cancelled! You didn't reply in time!",
                                color=Colours.wine_red()
                            )
                            await botmsg.edit(embed=error)

                        else:
                            await ctx.send(e)

                    else:
                        if um3.content == 'skip':
                            footer_content = None
                        elif um3.content != 'skip':
                            footer_content = um3.content
                        await um3.delete()

                        embed4 = nextcord.Embed(
                            title="Interactive Embed Setup",
                            description=f"What is the color of the embed? **Please reply in hex code format! Example: 0x7eebeb**\nTo have the color be orange, reply with `skip`!",
                            color=Colours.silver()
                        )
                        embed1.set_footer(text="You have 2 minutes to respond!")
                        await botmsg.edit(embed=embed4)

                        try:
                            um4 = await self.bot.wait_for('message', check=m_check, timeout=120.0)

                        except Exception as e:
                            if isinstance(e, asyncio.TimeoutError):
                                error = nextcord.Embed(
                                    description=f"Embed Setup Cancelled! You didn't reply in time!",
                                    color=Colours.wine_red()
                                )
                                await botmsg.edit(embed=error)

                            else:
                                await ctx.send(e)

                        else:
                            if um4.content == 'skip':
                                color_content = Colours.orange()
                            elif um4.content != 'skip':
                                color_content = int(f"{um4.content}", 0)
                            await um4.delete()

                            embed5 = nextcord.Embed(
                                title="Interactive Embed Setup",
                                description=f"What is the url of the image on the embed?\nTo have no image, reply with `skip`!",
                                color=Colours.silver()
                            )
                            embed1.set_footer(text="You have 2 minutes to respond!")
                            await botmsg.edit(embed=embed5)

                            try:
                                um5 = await self.bot.wait_for('message', check=m_check, timeout=120.0)

                            except Exception as e:
                                if isinstance(e, asyncio.TimeoutError):
                                    error = nextcord.Embed(
                                        description=f"Embed Setup Cancelled! You didn't reply in time!",
                                        color=Colours.wine_red()
                                    )
                                    await botmsg.edit(embed=error)

                                else:
                                    await ctx.send(e)

                            else:
                                if um5.content.lower() == 'skip':
                                    image_content = None
                                elif um5.content.lower() != 'skip':
                                    image_content = um5.content
                                await um5.delete()

                                embed6 = nextcord.Embed(
                                    title="Interactive Embed Setup",
                                    description=f"What is the id of the channel you want to send the embed in?\nTo have the embed in this channel, reply with `skip`!",
                                    color=Colours.silver()
                                )
                                embed1.set_footer(text="You have 2 minutes to respond!")
                                await botmsg.edit(embed=embed6)

                                try:
                                    um6 = await self.bot.wait_for('message', check=m_check, timeout=120.0)

                                except Exception as e:
                                    if isinstance(e, asyncio.TimeoutError):
                                        error = nextcord.Embed(
                                            description=f"Embed Setup Cancelled! You didn't reply in time!",
                                            color=Colours.wine_red()
                                        )
                                        await botmsg.edit(embed=error)

                                    else:
                                        await ctx.send(e)

                                else:
                                    if um6.content.lower() == 'skip':
                                        channel_id = ctx.channel
                                    elif um6.content.lower() != 'skip':
                                        cnl_id = int(um6.content, 0)
                                        channel_id = ctx.guild.get_channel(cnl_id)
                                    await um6.delete()

                                    sendembed = nextcord.Embed(
                                        title=title_content,
                                        description=desc_content,
                                        color=color_content
                                    )
                                    if image_content is not None:
                                        sendembed.set_image(url=image_content)

                                    if footer_content is not None:
                                        sendembed.set_footer(text=footer_content)

                                    await channel_id.send(embed=sendembed)

        elif text:
            embed = nextcord.Embed(description=text, color=color)
            content = None
            if ctx.message.attachments:
                content = await ctx.message.attachments[0].to_file()
                embed.set_image(url="attachment://" + str(content.filename))
            try:
                await channel.send(embed=embed, file=content if ctx.message.attachments else None)
            except:
                await ctx.send("I was unable to send the embed to this channel. Please make sure I have the correct read/send permissions for that channel!")

def setup(bot):
    bot.add_cog(sendembed(bot))
