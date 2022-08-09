import discord
import pytest
from pytest_mock import MockerFixture
import discord.ext.commands as commands
import discord.ext.test as dpytest
import src.main as main

@pytest.mark.asyncio
async def test_show_image(bot):
    guild = bot.guilds[0]
    channel = guild.text_channels[0]

    embed = discord.Embed(title="Test Image")
    embed.set_image(url="http://my_url_image.com/image")
    await channel.send(embed=embed)
    
    msg = await channel.history(limit=1).flatten()
    msg_embed = msg[0].embeds
    assert msg_embed[0].title == "Test Image"
    assert msg_embed[0].image.url == "http://my_url_image.com/image"
    
    embed = discord.Embed(title="Test Pic")
    embed.set_image(url="http://my_url_pic.com/pic")
    await channel.send(embed=embed)
    
    msg = await channel.history(limit=1).flatten()
    msg_embed = msg[0].embeds
    assert msg_embed[0].title.startswith("Test Pic")
    assert msg_embed[0].image.url.startswith("http://my_url_pic.com/pic")

def test_init(mocker: MockerFixture) -> None:
    mocker.patch.object(main, "__name__", "__main__")
    mocker.patch.object(main, 'main', return_value=None)
    spy = mocker.spy(main, 'main')

    assert main.init() == None
    assert spy.spy_return == None
    
    
