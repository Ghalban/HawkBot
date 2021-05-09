import discord
from discord.ext import commands
'''
  TODO:
    function is exclusive to 1 server bc I dont want to build databases :)
    format into sleeker looking embeds 
    guild = await bot.get_guild(ID)
'''
class ModmailCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
   
    @bot.event
    async def on_message(message):
        empty_array = []
        modmail_channel = discord.utils.get(bot.get_all_channels(), name="modmail")

        if message.author == bot.user:
            return

        if str(message.channel.type) == "private":
            if message.attachments != empty_array:
                files = message.attachments
                await modmail_channel.send("[" + message.author.display_name + "]")

                for file in files:
                    await modmail_channel.send(file.url)
            else:
                await modmail_channel.send("[" + message.author.display_name + "] " + message.content)

        elif str(message.channel) == "modmail" and message.content.startswith("<"):
            member_object = message.mentions[0]
            if message.attachments != empty_array:
                files = message.attachments
                await member_object.send("[" + message.author.display_name + "]")

                for file in files:
                    await member_object.send(file.url)
            else:
                index = message.content.index(" ")
                string = message.content
                mod_message = string[index:]
                await member_object.send("[" + message.author.display_name + "]" + mod_message)

        await bot.process_commands(message)  
        # Fixed no command process !!!! Keep this at end of on_message event function!!!!


def setup(bot):
  bot.add_cog(ModmailCog(bot))