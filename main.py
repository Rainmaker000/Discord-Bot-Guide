import discord
from discord.ext import commands

TOKEN = 'Your token'
PREFIX = '/'
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.command()
async def wassup(ctx):
    username = ctx.author.name
    await ctx.reply(f"wassup {username}")

bot.run(TOKEN)
