import os
import random
import discord
import giphy_client
from discord.ext import commands
from googleapiclient.discovery import build
from giphy_client.rest import ApiException

TOKEN = "YOUR TOKEN"  #Bot Token
google_search_api_key = "YOUR API KEY"  #Google API key
giphy_search_api_key = "YOUR API KEY"  #GIPHY API key
#cx is Google Search Engine ID

def main():
    client = commands.Bot(command_prefix="$")
    
    @client.event
    async def on_ready():
        print("!!! Bot Image Search Is Online !!!\n")

    @client.command(aliases=["show"])
    async def showpic(ctx, *, search):
        ran = random.randint(0, 9)
        resource = build("customsearch", "v1", developerKey=google_search_api_key).cse()
        result = resource.list(
            q=f"{search}", cx="YOUR ID GOOGLE SEARCH", searchType="image"
        ).execute()
        url = result["items"][ran]["link"]
        embed1 = discord.Embed(title=f"This is the image ({search}) you reserch|")
        embed1.set_image(url=url)
        await ctx.send(embed=embed1)
    
        api_instance = giphy_client.DefaultApi()
        try:
            api_responce = api_instance.gifs_search_get(giphy_search_api_key, q=f"{search}", limit=5, rating="g")
            lst = list(api_responce.data)
            giff = random.choice(lst)
            embed2 = discord.Embed(title=f"This is the gif ({search}) you reserch|")
            embed2.set_image(url=f'https://media.giphy.com/{giff.id}/giphy.gif')
            await ctx.send(giff.embed_url)
        except ApiException as e:
            print("Exception when calling API!")
    
    client.run(TOKEN)
if __name__ == "__main__":
    main()
