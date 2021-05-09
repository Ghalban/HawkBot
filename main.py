import discord
import os
import random
import sys, traceback

from keep_alive import keep_alive
from discord.ext import commands
from datetime import date



intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', help_command=None,intents=intents)

@bot.event  # Startup
async def on_ready():
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="for >help"))
    print("It's all here - Hawkbot successfully initialized!")

  
#===============================================================================================
#   DATA
#===============================================================================================

goodmorning = ["🇪🇸 Buenos días!",
    "🇮🇪 Top O' the mornin' to ya laddies!", "🇩🇪 Guten Morgen!",
    "No.", "🇮🇹 Buongiorno!", "Good morning!", "🇸🇦!صباح الخير", "🇯🇵 おはよう！\nhttps://res.cloudinary.com/animillust/video/upload/v1617837295/audio/weebohio_qyllfi.webm","https://youtu.be/03m9DzSEB5M", "https://youtu.be/5CGdX1hhxyo","https://youtu.be/8O27jMawP-o?t=11", "https://youtu.be/ii3NEUSiOdo","https://youtu.be/8nGcWFRwhOM"]

hello = [
    "Hello", "What’s shakin’?", "I'm here for you" "What’s up?", "Everything OK?", "Hey", "Yo", "Hi! (˵'v'˵)/ ", "Yes hello", "Can I help you?", "Sup?", "How are you doing fellow kid?",
    "Are you talking to me? Are you. Talking to. Me?", "eyo", "How have you been?", "How are ya?",
    "I'm watching you", "What?", "<:x_Susan:668503800947933184>", "Am birb.", "You called?", "What do you want?",
    "Ugh, not again...",
    "I̶̠̘̮͎̝̩̪͉̝̯̯̤̱͒̏̕͘̚͜͝ͅ ̴̢̮̰͔͓̪̱̺̺̤̮͛̂̊͜ḧ̸̡̝̘̦̭͇͓̣̺̰͍̭̲̫̝̇̽́a̵̤̹̍̽͊̅̀͌͜v̵̨̧̡̻̹̮͕̖̭̼͈̲̦̈́́̄̊̂̽̓̅̒̃̅͐͘͠͝e̴̡̨̛͚͇͔͙̻̯͔̹̫̮̫̙͗͗̍̊̇͐̂̀͘ ̷͕͚͍̦̲̯̥̱̼̩̪̠̐͑̃̈́͒͜͝ͅb̸̧̧̛̥͖̜̞̑͑͗̋̽̆͐ḛ̶͋́̑́̉̍̽̃̎͘e̴̘̣͎͉̰̮͚̙͓̮̥̥̹͛͜ͅn̷̘̥̖͓̗̭͎̹̖̯̗̩̯̙̣̊̈́ ̶̨̧̥̺̦̤̯̮̦̥̳̆̂̐s̴͉̥̒̔̃̓͊̇̏̃͑̿͐̕͝ú̴̡̺̫́̌̎̀̈́́͌́̈͘͘͝m̵̰̬̮̊̆̒̂̅̌͌͒͋͐͐̈́̊͘͠ḿ̶̤̜̥̥̣̙̿́̂̓͘͠ȏ̵͇̜̠̦̽̀̈́ń̸̨̰̪͖̗͍̞̀̿̄̑̔̒̕é̷͔͚̱͓͕͙̺̖͗̏̾̂͐̄d̸̒"
]

#This is a joke a i swear
threat = [
    "birdmeat", "birdbrain", "kick", "punch", "hate", "choke", "punk", "bitch",
    "scare", "fear", "break","shut", "menace", "uck", "buggy", "annoying", "mess",
    "stupid", "threat", "stink", "dum", "useless", "waste", "smell", "kill",
    "nasty","weeb", "gross", "end", "ugly", "poor", "narc"
]
retort1 = [
    "im gonna un-carbonate your soda if you dont be quiet",
    "Don't make me demonstrate how kneecaps are a privilege and not a human right",
    "Run.", "Now, now, no need to get nasty.", "Shut",
    "I love you too.", "Muhaha",
    "Why can't we be friends?", "Whatever",
    "You Shouldnt Have Said That.", "Haha!", "Hahahaha!",
    "Oh no you didnt just say that.", "Ouch.",
    "Hee hee!", "Wow. Just. Wow.",
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
]

apology = ["sorry", "apolog", "forgive"]
retort2 = [
    "All is forgiven", "Cool story bro", "K", "alright",
    "You're my friend now! (˵՞v՞˵)",
    "Ok... but I'll never forget what you did to me.", "we cool",
    "it's all water under the bridge now", "its ok, bots don't have feelings anyways"
]

praise = ["nice", "pretty", "smart", "best", "beautiful", "precious", "helpful", "handsome"]
praiseThank = [
  "Youre making me blush (˵>v<˵)","Why thank you :two_hearts:", "Youre too kind (˵•v•˵)",
   "Trying my best for you! :two_hearts:", ":^)", "(˵•v•˵)", "(˵>v<˵)", ":flushed::two_hearts:",":brown_heart:", ":two_hearts:"
  ]

youreWelcome = ["You're welcome!", "Happy to help!", "Always here when you need me... aside from downtime ( ͡° ͜ʖ ͡°)", "Anytime!", "Here to help!", "You're welcome, good luck out there!", "You got this!", "Anytime. Good luck out there! (˵՞v՞˵)✧", "Gotchu fam", "At your service :^)" ]

magicEightBall = [
    "As I see it, yes.", "Ask again later.", "Better not tell you now.",
    "Don't you know?", "Use that one braincell you have, damn.",
    "Your question caused me brain damage. Time for me to stop thinking today.",
    "Don’t count on it.", "It is certain.", "It is decidedly so.",
    "Most likely.", "My reply is no.", "Silence.", "You wouldnt wanna know",
    "Give me your credit card number first, then I'll answer you.", "My sources say no.",
    "Outlook not so good.", "Outlook good.", "Wouldnt you like to know?",
    "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.",
    "Without a doubt.", "Yes.", "Yes – definitely.", "You may rely on it.",
    "I can't believe you needed to ask that.", "Absolutely Not",
    "Did you really need to ask?", "Ask someone else.", "Seriously dude?",
    "Yeah.", "Urgh, can't think right now."
]

amBird = [
    "I'm a good bird (˵•v•˵)", "Tweet tweet~♩", "Chirp chirp~♩",
    "I'm the prettiest bird!~ (˵՞v՞˵)", "CA-CAW!!!", "Cheep cheep~♩",
    "I'm the coolest bird!", "I'm best bird",
    "https://media.giphy.com/media/iY93nyybFymvEOP48W/giphy.gif",
    "https://media.giphy.com/media/VBVY9IJKDxwHK/giphy.gif",
    "https://media.giphy.com/media/vmGJdiqLTG4lq/giphy.gif",
    "https://media.giphy.com/media/pCdmE1UoO8NZm/giphy.gif",
    "https://media.giphy.com/media/FxbXUFlFqRCjS/giphy.gif",
    "https://media.giphy.com/media/dYdGA39uJWMs0EJdy8/giphy.gif",
    "https://media.giphy.com/media/3oEjHXRXrssGd8z1fi/giphy.gif"
]

hints = ["asking HawkBot a question like \"Hawkbot, how old are you?\"", "saying something nice to hawkbot.. or not!", "reminding hawkbot it has poorly optimized code"]

#===============================================================================================
#   EVENTS and LISTENERS
#===============================================================================================

@bot.event  # Prevents feedback loop
async def on_message(message):
    if message.author == bot.user: return
    if message.author.bot: return

    await bot.process_commands(message)
    # Fixed no command process !!!! Keep this at end of on_message event functions!!!!

@bot.listen('on_message') # Listeners dont need await bot.process_commands(message), only events
async def badAI(message):
  userMessage = message.content.lower() #checked message converted to lowercase to process conditions met

  # Detect trigger words in data, only triggered if mentioned by name and not bot self
  if (("hawkbo" in userMessage) and (message.author != bot.user)):

  # Different Use Cases
  
    # Good Morning
        if 'good morning' in userMessage:
          await message.channel.send(random.choice(goodmorning))

    # Hawkbot gets Bullied
        elif any(word in userMessage for word in apology): #Apology case checked first
          await message.channel.send(random.choice(retort2))

        elif any(word in userMessage for word in threat): # Bully check second
          await message.channel.send(random.choice(retort1))
              
    # A Question
        elif "?" in userMessage:
          if 'how old' in userMessage:
            birthday = date(2021, 2, 26) 
            today = date.today()
            delta = today - birthday
            await message.channel.send(f"I manifested on {birthday}, so I'm {delta.days} days old!")
          else:
            await message.channel.send(random.choice(magicEightBall))

    # Complements and Thanks
        elif any(word in userMessage for word in praise):
          await message.channel.send(random.choice(praiseThank))
        elif "thank" in userMessage:
          await message.channel.send(random.choice(youreWelcome))

# Default response is hello
        else:
          await message.channel.send(random.choice(hello))

@bot.listen('on_message')
async def secrets(message):
  if message.author == bot.user: return
  if message.author.bot: return

  if "all here" in message.content.lower():
    await message.channel.send("It's all here! <:MSU:546838797153861652>")
    return;
  if "bird" in message.content.lower() or "birb" in message.content.lower():
    await message.channel.send(random.choice(amBird))
    return;
  if '...2' in message.content.lower(): #Peggle 2 E3 gif
    await message.channel.send("https://tenor.com/bdqG4.gif")
    return;

#===============================================================================================
#   COMMANDS
#===============================================================================================

@bot.command()
async def help(ctx):
  '''
    Shows what bot can do and overwrites default discord.py help command
  '''
  with open("cmds.md") as f:
      cmds = f.read()

  embed = discord.Embed(  
          color=0xd1190d)

  embed.add_field(name="**About**", value="This is a helper bot written with discord.py and hosted on replit.\nA work in progress. May go offline as its updated.\nIf you want to help build this bot or host it on your MSU student server you can contact Rawda on [Github](https://github.com/Ghalban/HawkBot)", inline=False)

  embed.add_field(name="**Commands**", value=cmds, inline=False) 

  embed.set_thumbnail(
        url=
        "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/281/white-question-mark_2754.png")
  
  embed.set_footer(
        text= "Try " + random.choice(hints),
        icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/twitter/53/electric-light-bulb_1f4a1.png')

  await ctx.send(embed=embed)

#================================================================================================
#   COGS https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html
#================================================================================================

initial_extensions = ['newsemester','search', 'info'] #modmail defunct till further notice 
for extension in initial_extensions:
    try:
        bot.load_extension(extension)
        print(f'Success! Loaded extension {extension}.')
    except:
        print(f'Failed to load extension {extension}.', file=sys.stderr)
    traceback.print_exc()

#===============================================================================================
#   KEEP BOT RUNNING
#===============================================================================================
keep_alive()
bot.run(os.getenv('TOKEN'))
bot = True
reconnect = True
