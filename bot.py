import discord
from discord import app_commands
from discord.ext import commands
import os
import google.generativeai as genai  # Gemini API

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
        response = await model.generate_content_async(question)  # Use async version
        answer = response.text if hasattr(response, 'text') and response.text else "I couldn't generate a response."
        await interaction.followup.send(f"**Question:** {question}\n**Answer:** {answer}")
    except Exception as e:
        await interaction.followup.send("❌ An error occurred while fetching the answer.")
        print(f"Error: {e}")
        
# Prefix command !ask
@bot.command(name="ask")
async def ask_prefix(ctx, *, question: str):
    async with ctx.typing():  # Show typing indicator
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = await model.generate_content_async(question)  # Use async version
            answer = response.text if hasattr(response, 'text') and response.text else "I couldn't generate a response."
            await ctx.send(f"**Question:** {question}\n**Answer:** {answer}")
        except Exception as e:
            await ctx.send("❌ An error occurred while fetching the answer.")
            print(f"Error: {e}")



# Run bot
bot.run(TOKEN)
