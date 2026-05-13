import discord
from discord.ext import tasks, commands
import asyncio
import random
import os

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
INTERVAL_MINUTES = int(os.getenv("INTERVAL_MINUTES", 30))

# Pegando a mensagem da variável do Railway
MESSAGE = os.getenv("MESSAGE", """🚀 **Anúncio padrão** (caso não configure a variável)""")

if not TOKEN or not CHANNEL_ID:
    print("❌ Falta configurar DISCORD_TOKEN ou CHANNEL_ID")
    exit(1)

CHANNEL_ID = int(CHANNEL_ID)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", self_bot=True, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Selfbot online como: {bot.user}")
    announce.start()

@tasks.loop(minutes=INTERVAL_MINUTES)
async def announce():
    try:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await asyncio.sleep(random.randint(0, 300))
            await channel.send(MESSAGE)
            print(f"✅ Mensagem enviada em: {channel.name}")
    except Exception as e:
        print(f"Erro: {e}")

bot.run(TOKEN)
