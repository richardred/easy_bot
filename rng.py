import random
from discord.ext import commands

class RNG():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def roll(self, ctx, *args):
        userID = ctx.message.author.id
        limit = 100
        if len(args) > 0:
            if args[0] == 'rick':
                await self.bot.say('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                return
            else:
                limit = int(args[0])

        userinfo = '<@%s> rolled ' % (userID)
        result = str(random.randint(0, limit))
        await self.bot.say(userinfo + result)

    @commands.command(pass_context=True)
    async def dice(self, ctx, *args : str):
        num_rolls = -1
        if len(args) == 0:
            num_rolls = 1
        else:
            num_rolls = int(args[0])
        userID = ctx.message.author.id
        userinfo = '<@%s> rolled ' % (userID)
        result = ', '.join(str(random.randint(1, 6)) for r in range(num_rolls))
        await self.bot.say(userinfo + result)
        
def setup(bot):
    bot.add_cog(RNG(bot))
