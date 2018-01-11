import discord
from discord.ext import commands

class Misc():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def info(self, ctx):
        emb = (discord.Embed(description='**Help menu**\n'
                             ':one: **osu! emoji/react**\n\t\t`[osu]`\n'
                             ':two: **Kenny\'s Social Security Number**\n\t\t`[$ssn]`\n'
                             ':three: **Roll**\n\t\t`[$roll, $roll number, $roll rick]`\n'
                             ':four: **Weebs**\n\t\t`[$amiweeb]`\n'
                             ':five: **Chromosomes**\n\t\t`[$chromosome]`\n'
                             ':six: **Most recent dota match info**\n\t\t`[$last]`\n'
                             ':seven: **Weather info**\n\t\t`[$weather city_name]`\n'
                             , color=0xAFAFAF))
        emb.set_author(name='Help', icon_url='http://www.atlantatrumpetensemble.com/images/junwoopark.jpg')
        await self.bot.say(embed=emb)

    @commands.command(pass_context=True)
    async def ssn(self, ctx):
        await self.bot.say('<@%s> 452-98-6521' % (92360169446473728))

def setup(bot):
    bot.add_cog(Misc(bot))
