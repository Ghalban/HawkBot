import discord
import requests

from discord.ext import commands
from bs4 import BeautifulSoup

class SearchCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        searchFilters = ['all', 'academic', 'department', 'page',
                         'people']  #incl alt forms

        #Search msu website
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

            # Get hits from website

            try:
                try:
                    hits = soup.find('div', {'class': 'result-count'}).text
                    print(hits)  # Extract number from hits..always first one
                    hitList = hits.split(
                    )  # Split hit string to [num,'results','found']
                    hits = hitList[0]  # override hits :^)
                except:
                    await ctx.send('Results not found! Try Google instead?\n[Be proactive! Report this bug here](https://github.com/Ghalban/HawkBot/issues)')
            except:
                await ctx.send(
                    'Something went wrong. Some code might not be up to date with the new MSU website, or MSU is blocking webscraping. [Be proactive! Report this bug here](https://github.com/Ghalban/HawkBot/issues)'
                )

            # Get links, titles, summaries from soup object
            if int(hits) > 0:
                links = []
                titles = []
                summaries = []
                listCap = 0;

                if int(hits) == 1:
                    listCap = 1
                    plurality = " result!"
                if int(hits) > 1:
                    if hits == 2:
                        listCap = 2
                    else:
                        listCap = 3
                    plurality = " results!"

                for result in soup.find_all('p', {'class': 'title'},
                                            limit=listCap):
                    a_tag = result.find('a')
                    links.append(a_tag.attrs['href'])
                    titles.append(result.find('a').get_text())
                    try:
                      summary_item = result.find_next_sibling('p')
                      summaries.append(summary_item.get_text())
                    except:
                      #print("looks like theres a missing element, lets fill it with a blank lol")
                      summaries.append('')
                
                count = 0;
                listing = ""
                while (count < listCap):
                  if ("https://www.montclair.edu" not in links[count]):
                    links[count] = "https://www.montclair.edu"+links[count]

                  listing = listing + (f"\n\n[**{titles[count]}**]({links[count]})\n{summaries[count]}")
                  # print(titles[count])
                  # print (summaries[count])
                  count = count + 1

                # print (listing)
                  
                embed = discord.Embed(
                    title=(f"Found {hits} {plurality}"),
                    url=url,
                    description=
                    (f"*Here's a snapshot of what I found.* [***Click here for more.***]({url}){listing}"
                     ),
                    color=0xd1190d)

                embed.set_thumbnail(
                    url=
                    "https://hotemoji.com/images/dl/m/left-pointing-magnifying-glass-emoji-by-twitter.png"
                )
                embed.set_footer(
                    text=
                    "To narrow search add one filter word from below after search terms:\npeople | page | department | academic",
                    icon_url=
                    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/twitter/53/electric-light-bulb_1f4a1.png"
                )
                links = []
                titles = []
                summaries = []
                await ctx.send(embed=embed)

            # Zero results
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
