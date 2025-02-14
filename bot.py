import discord
from discord.ext import commands
import random

# Enable intents
intents = discord.Intents.default()
intents.message_content = True  # This is crucial for responding to messages

# Create the bot with intents
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def roast(ctx, member: discord.Member = None):
    roasts = [
        "You're like a cloud. When you disappear, it's a beautiful day.",
        "You're proof that even evolution takes a step backward sometimes.",
        "You bring everyone so much joy… when you leave the room."
         "I'd explain it to you, but I left my crayons at home. 🖍️",
        "Your brain has more lag than a dial-up connection. 📡",
        "If stupidity was a sport, you'd be the MVP. 🏆",
        "Are you a black hole? Because you suck the intelligence out of the room. 🕳️",
        "You're proof that evolution sometimes hits the pause button. 🔄",
        "I've seen better logic in a potato. 🥔",
        "Your brain must be on airplane mode—zero connection. ✈️",
        "You bring everyone so much joy… when you leave the conversation. 😬",
        "I'd agree with you but then we'd both be wrong. 🤡",
        "Your birth certificate is an apology letter from the condom factory. 💀",
    ]

    if member:
        await ctx.send(f"{member.mention}, {random.choice(roasts)}")
    else:
        await ctx.send(random.choice(roasts))

# Run the bot
bot.run(TOKEN)
