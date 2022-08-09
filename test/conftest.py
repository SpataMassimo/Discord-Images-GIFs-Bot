import glob
import os
import pytest
import discord
import discord.ext.commands as commands
import discord.ext.test as test

@pytest.fixture
def bot(request, event_loop):
    intents = discord.Intents.default()
    intents.members = True
    b = commands.Bot("$", loop=event_loop, intents=intents)

    marks = request.function.pytestmark
    mark = None
    for mark in marks:
        if mark.name == "cogs":
            break
    if mark is not None:
        for extension in mark.args:
            b.load_extension("test.internal." + extension)
    test.configure(b)
    return b
