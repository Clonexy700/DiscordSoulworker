import discord
from discord.ext import commands

class basic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.client.user} has connected to Discord! I want to play a game!')
        await self.client.change_presence(activity=discord.Game(name='l!help | Soulworker'))

    @commands.command(name='ping', help=' - shows my ping')
    async def ping(self, ctx):
        embedping = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        embedping.add_field(name='My ping', value=f'Pong!{round(self.client.latency * 1000)}ms')
        await ctx.send(embed=embedping)


def setup(client):
    client.add_cog(basic(client))
