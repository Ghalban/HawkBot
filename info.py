import discord
from discord.ext import commands

class InfoCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
   
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

def setup(bot):
  bot.add_cog(InfoCog(bot))
