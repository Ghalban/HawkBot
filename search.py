import discord
import requests


from discord.ext import commands
from bs4 import BeautifulSoup
from pprint import pprint

class SearchCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    searchFilters = ['all', 'academic', 'department', 'page', 'people']  #incl alt forms
   
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

            # TODO case for 2 results
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

def setup(bot):
  bot.add_cog(SearchCog(bot))