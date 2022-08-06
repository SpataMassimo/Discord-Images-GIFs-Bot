import os
import random
import discord
from discord.ext import commands
from googleapiclient.discovery import build

TOKEN = "*Your token*"   #Bot Token
api_key = "*Your api-key*"  #Google API key
# cx is Google Search Engine ID

def main():
    client = commands.Bot(command_prefix="$")

    @client.event
    async def on_ready():
        print("!!! Bot Is Online !!!\n")


    @client.command(aliases=["show"])
    async def showpic(ctx, *, search):
        ran = random.randint(0, 9)
        resource = build("customsearch", "v1", developerKey=api_key).cse()
        result = resource.list(
            q=f"{search}", cx="*your cx*", searchType="image"
        ).execute()
        url = result["items"][ran]["link"]
        embed1 = discord.Embed(title=f"This is the image ({search}) you reserch|")
        embed1.set_image(url=url)
        await ctx.send(embed=embed1)

    client.run(TOKEN)

if __name__ == "__main__":
    main()