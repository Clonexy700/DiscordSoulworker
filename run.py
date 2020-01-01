import discord
from discord.ext import commands
client = commands.Bot(command_prefix='l!')
token = 0
f=open("token.txt", "r")
if f.mode == 'r':
    token = f.read()

client.run(token)
