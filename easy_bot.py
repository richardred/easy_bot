import discord
import sys, traceback
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()
bot = Bot(command_prefix="$", description = 'Richard\'s shitty bot')

startup_extensions = ['rng', 'roles', 'misc', 'weather', 'dota', 'maps']

@bot.event
async def on_message(message):
    if "osu" in message.content.lower().replace(' ', ''):
        osu1 = discord.utils.get(message.server.emojis, name = 'osu')
        if message.author != bot.user:
            await bot.send_message(message.channel, '<:osu:386018419276775434>')
        await bot.add_reaction(message, osu1)

    if 'junwoo' in message.content.lower().replace(' ', ''):
        junwoo = discord.utils.get(message.server.emojis, name = 'junwoo')
        if message.author != bot.user:
            await bot.send_file(message.channel, 'junwoo.png')
        await bot.add_reaction(message, junwoo)

    if '@everyone' in message.content.lower():
        await bot.send_file(message.channel, 'everyone.jpg')

    await bot.process_commands(message)


@bot.event
async def on_ready():
    print('\nLogged in as: ' + bot.user.name + ' (' + bot.user.id + ')\nVersion: ' + discord.__version__ + '\n')
    await bot.change_presence(game=discord.Game(name='Doki Doki Literature Club', type=1, url='https://github.com/richardred'))
    print('Successfully logged in and booted!')

if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception:
            print('Failed to load extension ' + extension + '.', file=sys.stderr)
            traceback.print_exc()

    bot.run('MzkyMTQxODM3MDUxMTAxMTg2.DRjAjQ.dZYXEHk5UbX1AOpUIMkwiPbVRAs', bot=True, reconnect=True)
