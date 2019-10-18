from configparser import ConfigParser
import discord
from discord.ext import commands

config = ConfigParser()
config.read('config.ini')

bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(config['DEFAULT']['token'])