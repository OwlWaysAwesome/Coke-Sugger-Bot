import discord
from discord import app_commands
from discord.ext import commands
import os
import google.generativeai as genai  # Gemini API
import random

# Load environment variables
TOKEN = os.getenv("TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize bot
intents = discord.Intents.default()
intents.message_content = True  # Ensure message content intent is explicitly enabled
bot = commands.Bot(command_prefix="!", intents=intents)

# Initialize Gemini API
genai.configure(api_key=GEMINI_API_KEY)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} commands")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

# Slash command: /ping
@bot.tree.command(name="ping", description="Check bot latency.")
async def ping_slash(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)  # Convert to ms
    await interaction.response.send_message(f"🏓 Pong! Latency: {latency}ms")

# Prefix command: !ping
@bot.command(name="ping")
async def ping_prefix(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"🏓 Pong! Latency: {latency}ms")

# Slash command: /ask
@bot.tree.command(name="ask", description="Ask a question to the AI.")
@app_commands.describe(question="What do you want to ask?")
async def ask_slash(interaction: discord.Interaction, question: str):
    await interaction.response.defer()
    try:
        model = genai.GenerativeModel("gemini-pro")
        prompt = f"You're a friendly, witty, and slightly sarcastic assistant. Respond in a casual, engaging, and humorous way when appropriate. Keep it human-like and avoid sounding robotic.\n\nUser: {question}\nYou:"
        response = model.generate_content(prompt)
        answer = response.text.strip() if response.text else "I couldn't generate a response."
        await interaction.followup.send(answer)
    except Exception as e:
        await interaction.followup.send("❌ An error occurred while fetching the answer.")
        print(f"Error: {e}")

# Prefix command: !ask
@bot.command(name="ask")
async def ask_prefix(ctx, *, question: str):
    await ctx.trigger_typing()
    try:
        model = genai.GenerativeModel("gemini-pro")
        prompt = f"You're a friendly, witty, and slightly sarcastic assistant. Respond in a casual, engaging, and humorous way when appropriate. Keep it human-like and avoid sounding robotic.\n\nUser: {question}\nYou:"
        response = model.generate_content(prompt)
        answer = response.text.strip() if response.text else "I couldn't generate a response."
        await ctx.send(answer)
    except Exception as e:
        await ctx.send("❌ An error occurred while fetching the answer.")
        print(f"Error: {e}")


# EXTREMELY brutal roasts 🔥😈
BRUTAL_ROASTS = [
    "You're like a software bug—annoying, useless, and nobody knows why you exist. 🐛",
    "You're so fake that even China wouldn't manufacture you. 🏭",
    "Your secrets are safe with me. I never even listen when you tell me them. 🙄",
    "If stupidity was a currency, you'd be a billionaire. 💸",
    "You're living proof that birth control isn't 100% effective. 😬",
    "You're like a cloud—white, fluffy, and completely useless. ☁️",
    "Your parents must have been eco-friendly… they recycled the worst traits into one person. ♻️",
    "You're slower than Internet Explorer on dial-up. 🐌💾",
    "You bring everyone so much happiness… when you shut up. 🤫",
    "I'd agree with you, but I don't talk to background characters. 🎭",
    "You're like a penny—cheap, two-faced, and barely worth anything. 🪙",
    "If I had a dollar for every smart thing you've ever said, I'd be broke. 💀",
    "You're proof that natural selection needs an update. 🔄",
    "You're the human equivalent of an expired milk carton. 🥛💀",
    "You should wear a mask—not for COVID, just for public safety. 😷",
    "You're like a math problem. Nobody likes you, and you're always too complicated.",
    "Your WiFi signal has more strength than your personality. 📶",
    "You're about as useful as a screen door on a submarine. 🚢",
    "Your voice is proof that even sound waves can be annoying. 🎤🚫",
    "You're the reason shampoo bottles have instructions. 🤦‍♂️",
    "You have something on your chin… no, the third one. 🏋️‍♂️",
    "Your life is like a broken pencil—pointless. ✏️",
    "You're so forgettable that even amnesia wouldn't help me remember you. 🧠❌",
    "I'd roast you harder, but I don't want to waste my best material on minor characters. 📖",
]

# Slash command: /roast
@bot.tree.command(name="roast", description="Unleash hell on someone.")
@app_commands.describe(user="The poor soul getting roasted.")
async def roast_slash(interaction: discord.Interaction, user: discord.Member):
    roast = random.choice(BRUTAL_ROASTS)
    await interaction.response.send_message(f"🔥 {user.mention}, {roast}")

# Prefix command: !roast
@bot.command(name="roast")
async def roast_prefix(ctx, user: discord.Member):
    roast = random.choice(BRUTAL_ROASTS)
    await ctx.send(f"🔥 {user.mention}, {roast}")

# Run bot
bot.run(TOKEN)
