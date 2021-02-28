import discord
import os
import requests
import sys, traceback

from keep_alive import keep_alive
from discord.ext import commands
from bs4 import BeautifulSoup
from pprint import pprint

intents = discord.Intents.default()
intents.members = True


#TODO write custom help command
bot = commands.Bot(command_prefix='!', intents=intents, description="This is a helper bot written with discord.py and hosted on repl.it\nA work in progress\nMay go offline as its updated.\n\nIf you want to help build this bot or host it on your MSU student server contact Rawda")

#Ping 
@bot.command()
async def ping(ctx):
    await ctx.send('Hello world')

#Test code
@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

#get server info
@bot.command()
async def info(ctx):
    guild = ctx.guild
    embed = discord.Embed(timestamp=ctx.message.created_at, color=0xd1190d)
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="Members", value=guild.member_count)
    embed.add_field(name="Region", value=guild.region, inline=True)
    embed.add_field(name="Owner", value=guild.owner, inline=True)
    embed.add_field(name="Created", value=guild.created_at, inline=True)
    embed.add_field(name="Channels", value=len(guild.channels), inline=True)
    embed.add_field(name="Roles", value=len(guild.roles), inline=True)
    embed.add_field(name="Boosters", value=guild.premium_subscription_count, inline=True)
    embed.set_author(name=f"{guild} | ID: {guild.id}", icon_url=guild.icon_url)
    embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

#Search msu website TODO clean this up and make into extention of main
@bot.command()
async def search(ctx, *, search, last=''):
    word_list = search.split()
    
    if word_list[-1]=='programs':
      word_list.pop()
      last=word_list[-1]
      word_list.pop()
    elif word_list[-1] == 'people':
      last = 'people'
      word_list.pop()
    elif word_list[-1] =='page' or 'pages':
      last = 'page'
      word_list.pop()
    elif word_list[-1] == 'department' or 'departments':
      last = 'department'
      word_list.pop()
    elif word_list[-1] == 'acedemic':
      last= 'academic'
      word_list.pop()
    elif word_list[-1]!= 'programs' or 'people' or 'department' or 'departments' or 'page' or 'pages':
      last='all'
    else:
      last = 'all'
      
    search = ' '.join(word_list)
    query_string = search.replace(' ', '%20')
    #Create url
    url = 'https://www.montclair.edu/search.php?q=' + query_string + '&filter=' + last + '&Submit=Search'
    #get page
    page=requests.get(url)
    #soup the page
    soup=BeautifulSoup(page.text, 'html.parser')
    pprint(soup)

    # get hits, 
    try:
        try:
            # get hits 
            hits = soup.find('div', {'class': 'result-count'}).text
           
        except:
            await ctx.send('Results not found! Try Google instead?')
    except:
        await ctx.send('Something went wrong. Please try again.')

    await ctx.send("*There are " + hits + ".*\n\n```You can add one of these filters after search term:\n\n      people\n      page\n      department\n      academic\n\n```" + url)

#List of things to scan for in messages

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
    print("It's all here")

allhere = ["its all here", "it's all here","depressing", "msu", "MSU", "It's all here", "Its all here", "calcia hall"]
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if any(word in message.content for word in allhere):
    await message.channel.send("It's all here! <:MSU:546838797153861652>")

#Cogs 
initial_extensions = ['cogs.modmail']
for extension in initial_extensions:
    try:
      bot.load_extension(extension)
      print(f'Loaded extension {extension}.')
    except:
      print(f'Failed to load extension {extension}.', file=sys.stderr)
    traceback.print_exc()

keep_alive()
bot.run(os.environ.get('TOKEN'))
bot=True
reconnect=True
