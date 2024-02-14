# Import necessary modules from discord.py
import discord
from discord.ext import commands

# Replace 'Your token' with your actual bot token
TOKEN = 'Your token'

# Set a custom command prefix for your bot
PREFIX = '/'

# Create an instance of Intents to enable certain privileged events
intents = discord.Intents().all()

# Create an instance of the bot with the specified command prefix and intents
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Define a simple command '/wassup'
@bot.command()
async def wassup(ctx):

# Get the username of the author who sent the command
  username = ctx.author.name
# Reply to the command with a greeting mentioning the user's name
  await ctx.reply(f"wassup {username}")

# Run the bot with the provided token
bot.run(TOKEN)
