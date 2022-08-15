import nextcord
from nextcord.ext import commands
import random
import asyncio
import math
from typing import Optional

class fun(commands.Cog, name='fun'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(description="Rolls a random number between 1 and 100. Check out the usage below to choose a custom dice.", ignore_extra=False)
    async def roll(self, ctx, min : int = None, max : int = None):
        if min and not max:
            return await ctx.send(f"⚠ That's not how you use this command! You must put two numbers. Example of usage: {ctx.prefix}roll 500 1000")
        if min == None:
            min = 100
        if max == min:
            return await ctx.send(f"⚠ The minimum and maximum numbers must not be the same! Example of usage: {ctx.prefix}roll 500 1000")
        if max:
            if min > max:
                return await ctx.send(f"⚠ The command errored. The minimum number must not be higher than the maximum number! Example of usage: {ctx.prefix}roll 500 1000")
        if min < 1:
            return await ctx.send(f"⚠ The command errored. You either set a number below 1, or you didn't set a maximum number! Example of usage: {ctx.prefix}roll 500 1000")
        if max is None:
            generated_num = random.randint(1, min)
        else:
            try:
                generated_num = random.randint(min,max)
            except ValueError:
                return await ctx.send(f"⚠ The command errored. You either set a number below 1, or you didn't set a maximum number! Example of usage: {ctx.prefix}roll 500 1000")
            else:
                generated_num = random.randint(min,max)
        await ctx.reply(f"Rolled **{generated_num}** out of **{max if max else 100}**.", mention_author=False, allowed_mentions=nextcord.AllowedMentions(everyone=False))
    
    @commands.command(name= '8ball', aliases=["ask"], description="Ask a question and get a yes/no response!")
    async def _8ball(self, ctx, *, question = None):

        if question is None:
            await ctx.send("You didn't ask me anything!")

        else:
            responses = ['It is certain.',
                         'It is decidedly so.',
                         'Without a doubt.',
                         'Yes - definitely.',
                         'You may rely on it.',
                         'As I see it, yes.',
                         'Most likely.',
                         'Outlook good.',
                         'My sources say yes',
                         'Yes.',
                         'Signs point to yes.',
                         'Reply hazy, try again.',
                         'Ask again later.',
                         'Better not tell you now.',
                         'Cannot predict now.',
                         'Concentrate and ask again.',
                         "Don't count on it.",
                         'My reply is no.',
                         'My sources say no.',
                         'Outlook not so good.',
                         'Yeah..... not happening.',
                         'Very doubtful.']

            answer = random.choice(responses)

            embed = nextcord.Embed(
                description=f"You Asked: **{question}**\n" +
                f"My Answer is: **{answer}**",
                color=0xb36720
            )

            await ctx.reply(embed=embed, mention_author=False, allowed_mentions=nextcord.AllowedMentions(everyone=False))
    
    @commands.command(description="Have the bot rate whatever you want!")
    async def rate(self, ctx, *, thing = None):
        """ Rates what you desire """
        if thing is None:
            rate_amount = random.uniform(0.0, 100.0)
            await ctx.reply(f"Since you didn't define anything to rate, I will rate you instead! Hmm... I rate you a **{round(rate_amount, 2)}** out of **100**! (But you'll always be a qt to me owo <3)", mention_author=False)
        elif thing is not None:
            rate_amount = random.uniform(0.0, 100.0)
            await ctx.reply(f"I'd rate '**{thing}**' a solid **{round(rate_amount, 2)}** out of **100**!", allowed_mentions=nextcord.AllowedMentions(everyone=False, roles=False, users=True), mention_author=False)

    @commands.command(name= 'coinflip', aliases=["flip"], description="Flips a coin that either results in heads or tails.")
    async def coinflip(self, ctx):

        check = "✅"
        cross = "❌"

        responses = ['It landed on **Heads**!',
                     'It landed on **Tails**!']

        choice = random.choice(responses)

        flipMSG = await ctx.reply(f'Flipping a coin...', mention_author=False)
        await asyncio.sleep(3)
        await flipMSG.edit(content=choice)
        await asyncio.sleep(1)
        message = await ctx.send(f'Would you like me to flip the coin again? React with {check} for yes, or {cross} for no.')
        await message.add_reaction(check)
        await message.add_reaction(cross)

        def react_check(reaction, user):
            if user == ctx.author and reaction.emoji == check:
                return True
            elif user == ctx.author and reaction.emoji == cross:
                return True
            else:
                return False

        try:
            reaction, user = await self.bot.wait_for("reaction_add", check=react_check, timeout=60*5)
        except Exception as e:
            if isinstance(e, asyncio.TimeoutError):
                await message.delete()
            else:
                await ctx.send(e)

        else:
            if reaction.emoji == check:
                await message.clear_reactions()
                await message.delete()
                await ctx.reinvoke()
            elif reaction.emoji == cross:
                await message.delete()
    
    @commands.command(description="User specific command")
    async def fran(self, ctx):
        if ctx.author.id==538700574426791946: #UserID of the person you want to be able to use the command
            response = random.choice([f"Hi Fran!", "Access granted!", "My calculations predict that you are indeed the person I am looking for. Hello, Fran."])
            await ctx.reply(response, mention_author=False)
        else:
            response = random.choice([f"Access denied. Only Fran can use this command.", "Sorry, but you're not Fran.", "My calculations predict you are not the person I am looking for. Only Fran may use this command."])
            return await ctx.reply(response, mention_author=False)

def setup(bot):
    bot.add_cog(fun(bot))
