import discord
import os
from discord.ext import commands
client = commands.Bot(command_prefix='l!')

for filename in os.listdir('./backend/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'backend.cogs.{filename[:-3]}')

token = 0
f = open("token.txt", "r")
if f.mode == 'r':
    token = f.read()


client.run(token)
