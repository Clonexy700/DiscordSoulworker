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

    @commands.command(name='github', help=' - sends github Lilly Bloommerchen link')
    async def github(self, ctx):
        github = discord.Embed(
            color=discord.Colour.dark_purple()
        )
        github.add_field(name='Github', value='https://github.com/Clonexy700')
        await ctx.send(embed=github)


def setup(client):
    client.add_cog(basic(client))
