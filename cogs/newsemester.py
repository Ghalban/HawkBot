import discord
from discord.ext import commands

class NewSemesterCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
   
    @bot.command()
    async def links(ctx):

      '''
      Links to help students start a new semester at MSU
      '''
      embed = discord.Embed(
            title="All in one place!",
            description=
            "*Click the pretty blue hyperlinks to go places*",
            color=0xd1190d)
            
      embed.set_thumbnail(
            url=
            "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/twitter/281/spiral-calendar_1f5d3-fe0f.png")

      embed.add_field(name="Scheduling",
                        value="➤ [Coursicle](https://www.coursicle.com/montclair/) rapid semester planning\n➤ [Banner](https://student-ssb-regis.montclair.edu/StudentRegistrationSsb/ssb/registration) register for classes\n➤ [Important Deadlines](https://www.montclair.edu/student-services/important-dates/)",
                        inline=False)

      embed.add_field(name="Financial Aid",
                        value="➤ [FAFSA](https://fafsa.ed.gov/spa/fafsa/#/LOGIN?locale=en_US) Federal Student Aid\n➤ [HESSA](https://njfams.hesaa.org/NJFAMS/login.aspx) New Jersey Student Aid",
                        inline=False)

      embed.add_field(name="Commuters",
                        value="➤ [Parking Permits](https://montclairstate.t2hosted.com/cmn/auth.aspx) \n➤ [NJ Transit Student Discount Portal](https://njtransit.montclair.edu/njtransit/servlet) ",
                        inline=False)

      await ctx.send(embed=embed)
      

def setup(bot):
  bot.add_cog(NewSemesterCog(bot))