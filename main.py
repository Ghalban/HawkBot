import discord
import os
import random
import requests
import sys, traceback

from keep_alive import keep_alive
from discord.ext import commands
from bs4 import BeautifulSoup
from pprint import pprint


intents = discord.Intents.default()
intents.members = True

#TODO write custom help command
bot = commands.Bot(
    command_prefix='>',
    intents=intents,
    description=
    "This is a helper bot written with discord.py and hosted on repl.it\nA work in progress\nMay go offline as its updated.\n\nIf you want to help build this bot or host it on your MSU student server contact Rawda"
)

#================================================================================================
#   DATA
#================================================================================================

allhere = [
    "all here",
    " depressing"
] 

searchFilters = [
    'all', 'academic', 'department', 'page', 'people', '', '\n', ' '
]  #incl alt forms

goodmorningMessage = ["say good morning", "good morning"]

goodmorning = [
    "Guwud moworning!", "🇪🇸 Buenos días!",
    "🇮🇪 Top O' the mornin' to ya laddies!", "🇩🇪 Guten Morgen!",
    "No.", "🇮🇹 Buongiorno!", "Good morning!",
    "🇯🇵 おはよう！\nhttps://res.cloudinary.com/animillust/video/upload/v1617837295/audio/weebohio_qyllfi.webm",
    "https://youtu.be/03m9DzSEB5M", "https://youtu.be/5CGdX1hhxyo",
    "https://youtu.be/8O27jMawP-o?t=11", "https://youtu.be/ii3NEUSiOdo",
    "https://youtu.be/8nGcWFRwhOM"
]

hawkbott = ["hawkboy", "hawkbot", "hawkboi"]
hello = [
    "Hello", "Hey", "Hi! (˵'v'˵)/ ", "Yes hello",
    "Are you talking to me? Are you. Talking to. Me?", "eyo",
    "I'm watching you", "What?", "<:x_Susan:668503800947933184>", "Am birb.",
    "Hello darkness my old friend ♩", "You called?", "What do you want",
    "Ugh, not again...",
    "I̶̠̘̮͎̝̩̪͉̝̯̯̤̱͒̏̕͘̚͜͝ͅ ̴̢̮̰͔͓̪̱̺̺̤̮͛̂̊͜ḧ̸̡̝̘̦̭͇͓̣̺̰͍̭̲̫̝̇̽́a̵̤̹̍̽͊̅̀͌͜v̵̨̧̡̻̹̮͕̖̭̼͈̲̦̈́́̄̊̂̽̓̅̒̃̅͐͘͠͝e̴̡̨̛͚͇͔͙̻̯͔̹̫̮̫̙͗͗̍̊̇͐̂̀͘ ̷͕͚͍̦̲̯̥̱̼̩̪̠̐͑̃̈́͒͜͝ͅb̸̧̧̛̥͖̜̞̑͑͗̋̽̆͐ḛ̶͋́̑́̉̍̽̃̎͘e̴̘̣͎͉̰̮͚̙͓̮̥̥̹͛͜ͅn̷̘̥̖͓̗̭͎̹̖̯̗̩̯̙̣̊̈́ ̶̨̧̥̺̦̤̯̮̦̥̳̆̂̐s̴͉̥̒̔̃̓͊̇̏̃͑̿͐̕͝ú̴̡̺̫́̌̎̀̈́́͌́̈͘͘͝m̵̰̬̮̊̆̒̂̅̌͌͒͋͐͐̈́̊͘͠ḿ̶̤̜̥̥̣̙̿́̂̓͘͠ȏ̵͇̜̠̦̽̀̈́ń̸̨̰̪͖̗͍̞̀̿̄̑̔̒̕é̷͔͚̱͓͕͙̺̖͗̏̾̂͐̄d̸̒"
]

#This is a joke a i swear
threat = [
    "birdmeat", "birdbrain", "kick", "punch", "hate", "choke", "punk", "bitch",
    "scare", "fear", "break","shut", "menace", "uck",
    "stupid", "threat", "stink", "dum", "useless", "waste", "smell", "kill",
    "nasty","weeb", "gross", "end", "quiet", "ice"
]
retort1 = [
    "im gonna un-carbonate your soda if you dont shut up",
    "Don't make me demonstrate how kneecaps are a privilege and not a human right",
    "Run.", "Now, now, no need to get nasty.", "Shut",
    "I love you too.",
    "Why can't we be friends?", "Whatever",
    "You Shouldnt Have Said That.", "Haha!", "Hahahaha!",
    "Oh no you didnt just say that.", "Ouch.",
    "Hee hee!", "Wow. Just. Wow.",
    "Don't make me make you drink wet sand from a boot.",
    "Give me your lunch money.",
    "Don't make me rearrange every single one of your atoms",
    "Don't say that.", "Tee hee!", "Teeheehee!",
    "I can't hear you.", "What did you say, punk?",
    "Enjoy your next 24 hours.",
    "I hope both sides of your pillow are warm tonight",
    "Don't make me force you to manually breathe", "Say that again, punk.",
    "Stop it.",
    "Take that back", "Seriously dude? Seriously?",
    "Don't make me break your bones in alphabetical order.",
    "I would like you to apologize on behalf of the human race.",
    "https://media.giphy.com/media/VBVY9IJKDxwHK/giphy.gif",
    "https://media.giphy.com/media/vmGJdiqLTG4lq/giphy.gif",
    "https://media.giphy.com/media/pCdmE1UoO8NZm/giphy.gif"
]

apology = ["sorry", "apolog", "forgive"]
retort2 = [
    "All is forgiven", "Cool story bro", "K", "alright",
    "You're my friend now! (˵՞v՞˵)",
    "Ok... but I'll never forget what you did to me.", "we cool",
    "it's all water under the bridge now", "its ok, bots don't have feelings anyways."
]

questioning = ["?", "is", "are"]
magicEightBall = [
    "As I see it, yes.", "Ask again later.", "Better not tell you now.",
    "Don't you know?", "Use that one braincell you have, damn.",
    "Your question caused me brain damage. Time for me to stop thinking today.",
    "Don’t count on it.", "It is certain.", "It is decidedly so.",
    "Most likely.", "My reply is no.", "Shut up.",
    "Give me your credit card number first, then I'll answer you.", "My sources say no.",
    "Outlook not so good.", "Outlook good.", "Wouldnt you like to know?",
    "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.",
    "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it.",
    "I can't believe you needed to ask that.", "Absolutely Not",
    "Did you really need to ask?", "Ask someone else.", "Seriously dude?",
    "Yeah.", "Urgh, can't think right now."
]

bird = [" birb", " bird"]
ambird = [
    "Am birb (˵•v•˵)", "Tweet tweet~♩", "Chirp chirp~♩",
    "I'm the prettiest bird!~ (˵՞v՞˵)", "CA-CAW", "Cheep cheep~♩",
    "I'm the coolest bird!", "I'm best bird", "I wish I were a bird",
    "https://media.giphy.com/media/iY93nyybFymvEOP48W/giphy.gif",
    "https://media.giphy.com/media/VBVY9IJKDxwHK/giphy.gif",
    "https://media.giphy.com/media/vmGJdiqLTG4lq/giphy.gif",
    "https://media.giphy.com/media/pCdmE1UoO8NZm/giphy.gif",
    "https://media.giphy.com/media/FxbXUFlFqRCjS/giphy.gif",
    "https://media.giphy.com/media/dYdGA39uJWMs0EJdy8/giphy.gif",
    "https://media.giphy.com/media/3oEjHXRXrssGd8z1fi/giphy.gif"
]

sOs = [
    "hello darkness, my old friend", "i've come to talk with you again",
    "because a vision softly creeping", "left its seeds while i was sleeping",
    "and the vision that was planted in my brain", "still remains",
    "within the sound of silence", "in restless dreams i walked alone",
    "narrow streets of cobblestone", "'neath the halo of a street lamp",
    "i turned my collar to the cold and damp",
    "when my eyes were stabbed by the flash of a neon light",
    "that split the night,"
    "and touched the sound of silence", "and in the naked light",
    "i saw,ten thousand people, maybe more", "people talking without speaking",
    "people hearing without listening",
    "people writing songs that voices never share", "and no one dared",
    "disturb the sound of silence"
]

#================================================================================================
#   EVENTS and LISTENERS
#================================================================================================

@bot.event  # Startup
async def on_ready():
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="you"))
    print("It's all here")


@bot.event  # Prevents feedback loop
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)
    # Fixed no command process !!!! Keep this at end of on_message event function!!!!


@bot.listen('on_message')
async def babble(message):
    if any(word in message.content.lower() for word in allhere):
        if message.author == bot.user:
            return  # Prevents feedback loop
        else:
            await message.channel.send(
                "It's all here! <:MSU:546838797153861652>")

    #mentioned = f'<@{bot.user.id}>'
    #if mentioned in message.content:
    if bot.user.mentioned_in(message):
        await message.channel.send(
            f"{random.choice(hello)}\nEnter ` >help ` for more info.")
        await bot.process_commands(message)
        # Fixed no command process !!!! Keep this at end of on_message event function!!!!


@bot.listen('on_message')
async def badAI(message):
    #Detect trigger words in data, only triggered if mentioned by name
    if any(word in message.content.lower()
           for word in hawkbott) or any(word in message.content.lower()
                                        for word in bird):
        #First check if message sent by self, if true return
        if message.author == bot.user:
            return  # Prevents feedback loop
            await bot.process_commands(message)

    #Next different use cases
    # Good morning
        elif any(word in message.content.lower()
                 for word in goodmorningMessage):
            if message.author == bot.user:
                return  # Prevents feedback loop
            else:
                await message.channel.send(random.choice(goodmorning))
                await bot.process_commands(message)

        elif any(word in message.content.lower() for word in apology):
            if message.author == bot.user:
                return  # Prevents feedback loop
            else:
                await message.channel.send(random.choice(retort2))
                await bot.process_commands(message)

        elif any(word in message.content.lower() for word in threat):
            if message.author == bot.user:
                return  # Prevents feedback loop
            else:
                await message.channel.send(random.choice(retort1))
                await bot.process_commands(message)

        elif any(word in message.content.lower() for word in questioning):
            if message.author == bot.user:
                return  # Prevents feedback loop
            else:
                await message.channel.send(random.choice(magicEightBall))
                await bot.process_commands(message)

        #Default response is hello
        else:
            await message.channel.send(random.choice(hello))
            await bot.process_commands(message)

    if any(word in message.content.lower() for word in bird):
        if message.author == bot.user:
            return  # Prevents feedback loop
        else:
            await message.channel.send(random.choice(ambird))
            await bot.process_commands(message)


@bot.listen('on_message')
async def soundOfSilence(message):
    index = 0
    if any(lyric in message.content.lower() for lyric in sOs):
        if message.author != bot.user:
            if index != len(sOs) - 1:
                index = sOs.index(message.content.lower()) + 1
                await message.channel.send(sOs[index])
                await bot.process_commands(message)


#================================================================================================
#   COMMANDS
#================================================================================================


@bot.command()
async def ping(ctx):
    '''
    Checks if bot is alive
    '''
    await ctx.send('Hello world')


@bot.command()
async def info(ctx):
    '''
    Returns server stats
    '''
    guild = ctx.guild
    embed = discord.Embed(timestamp=ctx.message.created_at, color=0xd1190d)
    embed.set_thumbnail(url=guild.icon_url)
    embed.add_field(name="Members", value=guild.member_count)
    embed.add_field(name="Region", value=guild.region, inline=True)
    embed.add_field(name="Owner", value=guild.owner, inline=True)
    embed.add_field(name="Created", value=guild.created_at, inline=True)
    embed.add_field(name="Channels", value=len(guild.channels), inline=True)
    embed.add_field(name="Roles", value=len(guild.roles), inline=True)
    embed.add_field(name="Boosters",
                    value=guild.premium_subscription_count,
                    inline=True)
    embed.set_author(name=f"{guild} | ID: {guild.id}", icon_url=guild.icon_url)
    embed.set_footer(
        text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}",
        icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


#Search msu website
#TODO iron out kinks in scraper ueaaaaaaaaaaaaaaaaaa
#TODO clean this up and move search to cogs folder (reformat as cog)

@bot.command()
async def search(ctx, *, search):
    '''
    Returns 3 search results scraped from MSU hawkeye search
    '''
    word_list = search.split()
    last = word_list[-1]

    if last not in searchFilters:
        last = 'all'

    else:
        last = word_list[-1]
        word_list.pop()

    search = ' '.join(word_list)
    query_marker = '%20'.join(word_list)

    # Create url

    url = 'https://www.montclair.edu/search.php?q=' + query_marker + '&filter=' + last + '&Submit=Search'

    # Get page

    page = requests.get(url)

    # Soup the page

    soup = BeautifulSoup(page.text, 'html.parser')
    pprint(soup)

    # Get hits from website

    try:
        try:
            hits = soup.find('div', {'class': 'result-count'}).text
            print(hits)  # Extract number from hits..always first one
            hitList = hits.split(
            )  # Split hit string to [num,'results','found']
            hits = hitList[0]  # override hits :^)
        except:
            await ctx.send('Results not found! Try Google instead?')
    except:
        await ctx.send('Something went wrong. Please try again.')

    if int(hits) > 0:
        if int(hits) == 1:
            plurality = " result!"
        if int(hits) > 1:
            plurality = " results!"

        embed = discord.Embed(
            title="Found " + hits + plurality,
            url=url,
            description=
            "Here's a snapshot of what I found. Click here for more.",
            color=0xd1190d)
        embed.set_thumbnail(
            url=
            "https://hotemoji.com/images/dl/m/left-pointing-magnifying-glass-emoji-by-twitter.png"
        )
        embed.add_field(name="Result 1",
                        value="someone needs to write a for loop",
                        inline=False)
        embed.add_field(name="Result 2",
                        value="that grabs THREE results from the site",
                        inline=False)
        embed.add_field(name="Result 3",
                        value="but thats for another day",
                        inline=False)
        embed.set_footer(
            text=
            "To narrow search add one filter word from below after search terms:\npeople | page | department | academic",
            icon_url=
            "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/twitter/53/electric-light-bulb_1f4a1.png"
        )
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title="There's no results.",
            url=url,
            description=
            (f"\n\nSorry, I couldnt find anything that matched ` {search} ` on HawkEye Search."
             ),
            color=0xd1190d)
        embed.add_field(
            name="Consider trying:",
            value=
            "➤ changing your keywords\n➤ checking Google results under HawkEye Search linked below",
            inline=False)
        embed.set_thumbnail(
            url=
            "https://hotemoji.com/images/dl/m/left-pointing-magnifying-glass-emoji-by-twitter.png"
        )
        await ctx.send(embed=embed)
        await ctx.send(url)

#================================================================================================
#   COGS
#================================================================================================

initial_extensions = ['cogs.modmail','cogs.newsemester',]
for extension in initial_extensions:
    try:
        bot.load_extension(extension)
        print(f'Loaded extension {extension}.')
    except:
        print(f'Failed to load extension {extension}.', file=sys.stderr)
    traceback.print_exc()

#================================================================================================
#   KEEP BOT RUNNING
#================================================================================================

keep_alive()
bot.run(os.getenv('TOKEN'))
bot = True
reconnect = True
