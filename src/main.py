import discord
import giphy_client
from discord.ext import commands
from googleapiclient.discovery import build
from giphy_client.rest import ApiException

TOKEN="Your token"
google_search_api_key = "YOUR API KEY" 
giphy_search_api_key = "YOUR API KEY"

def main():
    client = commands.Bot(command_prefix="$")
    
    @client.command(aliases=["show"])
    async def show_image(ctx, *, search):
        url =  ((build("customsearch", "v1", developerKey=google_search_api_key).cse()).list(q=f"{search}", cx="YOUR GOOGLE ID", searchType="image").execute())["items"][0]["link"]
        await ctx.send(embed = (discord.Embed(title=f"This is the image ({search}) you reserch|").set_image(url=url)))
        api_instance = giphy_client.DefaultApi()
        try:
            lst = list((api_instance.gifs_search_get(giphy_search_api_key, q=f"{search}", limit=1, rating="g")).data)
            embed = discord.Embed(title=f"This is the gif ({search}) you reserch|").set_image(url=f'https://media.giphy.com/{lst[0].id}/giphy.gif')
            await ctx.send(lst[0].embed_url)
        except ApiException as e:
            print("Exception when calling API!")
    client.run(TOKEN)
def init():
    if __name__ == '__main__':
        main() 

init()
