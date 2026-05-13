import discord
from discord.ext import tasks, commands
import asyncio
import random
import os

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
INTERVAL_MINUTES = int(os.getenv("INTERVAL_MINUTES", 30))

MESSAGE = """🚀 **Anúncio do meu produto!**

Meu produto incrível está em promoção! 
Link: https://seusite.com

Qualquer dúvida chama no PV!"""

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
            await asyncio.sleep(random.randint(0, 300))  # até 5 min de variação
            await channel.send(MESSAGE)
            print(f"✅ Mensagem enviada em {channel.name}")
    except Exception as e:
        print(f"Erro: {e}")

bot.run(TOKEN, bot=False)
