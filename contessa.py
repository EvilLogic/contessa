from configparser import ConfigParser
import discord
from discord.ext import commands

config = ConfigParser()

bot = commands.Bot(command_prefix='&')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(config['DEFAULT']['token'])