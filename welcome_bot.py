import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True  
intents.presences = True  
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='welcome-channel')
    if channel:
        await channel.send(f'Welcome to the server, {member.name}!')

bot.run(TOKEN)
