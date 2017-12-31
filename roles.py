from discord.ext import commands

class Roles():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def amiweeb(self, ctx):
        if '334558616088477697' in [role.id for role in ctx.message.author.roles]:
            await self.bot.say('Yes, you are a weeb.')
        else:
            await self.bot.say('No, you are not a weeb.')

    @commands.command(pass_context=True)
    async def chromosome(self, ctx):
        if '276577720388026379' in [role.id for role in ctx.message.author.roles]:
            await self.bot.say('You have 47 chromosomes.')
        else:
            await self.bot.say('You have 46 chromosomes.')
            
def setup(bot):
    bot.add_cog(Roles(bot))
