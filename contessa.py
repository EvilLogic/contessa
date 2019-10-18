from configparser import ConfigParser
from elo import Rating, rate_1vs1
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

def update_config():
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def is_new_player(player):
    if player not in config['SCORES']:
        return True
    return False

def add_new_player(player):
    config['SCORES'][player] = '1000'

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    # or to reply in a different channel
    # non-score commands should not be processed
    if (message.channel.name not in config['DEFAULT']['channel'] or
    message.author == bot.user or not message.content.startswith('&score')):
        return

    # Make a list of all the players
    args = message.content.split(' ')
    rankings = args[1:]

    # Make sure every player has a score
    for i in rankings:
        if is_new_player(i):
            add_new_player(i)
            await message.channel.send(i + ' added')
    update_config()

    for i in range(0, len(rankings)-1):
        #Create Ratings objects for each player
        winner, loser = Rating(float(config['SCORES'][rankings[i]])), Rating(float(config['SCORES'][rankings[i+1]]))

        # Return elo results of game
        winner, loser = rate_1vs1(winner, loser)

        # Assign new elos
        config['SCORES'][rankings[i]] = str(winner)
        config['SCORES'][rankings[i + 1]] = str(loser)

    # Print out the results
    msg = ''
    for i in rankings:
        msg += i + ' is now rank ' + str(config['SCORES'][i])[:6] + '\n'
    await message.channel.send(msg)
    update_config()

bot.run(config['DEFAULT']['token'])