import discord
from discord.exe import command
import music 

cogs = [music]

client = commands.BOT (command_prefix='prefix', intents = discord..intents.all())

for i in range(len(cogs)):
    cogs[i].setup()





client.run("TOKEN")
