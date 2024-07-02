import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()
# Define the bot token (Keep this secure)
TOKEN = os.getenv('TOKEN')

# Set the command prefix and intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the bot to read message content

bot = commands.Bot(command_prefix='!', intents=intents)


# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')


# Command: Ping
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')


# Command: Say hello
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')


# Command: Say goodbye
@bot.command(name='goodbye')
async def goodbye(ctx):
    await ctx.send(f'Goodbye {ctx.author.mention}!')


# Command: Add two numbers
@bot.command(name='add')
async def add(ctx, num1: float, num2: float):
    result = num1 + num2
    await ctx.send(f'The sum of {num1} and {num2} is {result}')


# Command Error Handler: To catch any command-related errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I didn't recognize that command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You're missing some required arguments for this command.")
    else:
        await ctx.send("An error occurred while processing the command.")
        raise error


# command to help and tell about available commands
@bot.command(name='guide')
async def guide(ctx):
    await ctx.send("```Available commands:\n!ping\n!hello\n!goodbye\n!add <num1> <num2>```")


# Run the bot
bot.run(TOKEN)
