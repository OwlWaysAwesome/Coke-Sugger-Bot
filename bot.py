import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv  # Load environment variables

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")  # Read the token from .env

if TOKEN is None:
    print("❌ ERROR: DISCORD_TOKEN is not set!")
    exit()

# Enable intents
intents = discord.Intents.default()
intents.message_content = True  # Ensure this is enabled
intents.guilds = True
intents.members = True

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_message(message):
    print(f"📩 Message received: {message.content} from {message.author}")  # Debugging
    await bot.process_commands(message)  # Allow command processing

@bot.command()
async def roast(ctx, member: discord.Member = None):
    roasts = [
        "You're like a cloud. When you disappear, it's a beautiful day.",
        "You're proof that even evolution takes a step backward sometimes.",
        "You bring everyone so much joy… when you leave the room."
    ]
    if member:
        await ctx.send(f"{member.mention}, {random.choice(roasts)}")
    else:
        await ctx.send(random.choice(roasts))

# Run the bot
bot.run(TOKEN)
