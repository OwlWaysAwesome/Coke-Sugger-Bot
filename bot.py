import discord
from discord.ext import commands
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Google Gemini AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Bot setup
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Slash command setup
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ask(ctx, *, question):
    """Ask the AI a question"""
    response = model.generate_content(question)
    await ctx.send(response.text)

# Keep-alive function (if hosting on Railway)
try:
    from keep_alive import keep_alive
    keep_alive()
except ImportError:
    pass

# Run the bot
bot.run(TOKEN)
