import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load .env file (useful for local testing)
load_dotenv()

# Fetch token from environment variables
TOKEN = os.getenv("TOKEN")

# Debugging: Check if TOKEN is loading
if not TOKEN:
    print("❌ TOKEN not found. Make sure it's set in Railway Variables!")
    exit(1)  # Exit the script if no token is found
else:
    print(f"✅ TOKEN loaded successfully!")

# Set up bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Run bot
bot.run(TOKEN)
