import discord
from discord.ext import tasks, commands
import asyncio
import random
import os

# ================= CONFIGURAÇÃO =================
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
INTERVAL_MINUTES = int(os.getenv("INTERVAL_MINUTES", 30))

if not TOKEN:
    print("❌ ERRO: DISCORD_TOKEN não foi configurado!")
    exit(1)

if not CHANNEL_ID:
    print("❌ ERRO: CHANNEL_ID não foi configurado!")
    exit(1)

CHANNEL_ID = int(CHANNEL_ID)

MESSAGE = """🚀 **Anúncio do meu produto!**

Meu produto incrível está em promoção! 
Link: https://seusite.com

Qualquer dúvida chama no PV!"""
# ================================================

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", self_bot=True, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Selfbot online como: {bot.user}")
    print(f"📍 Anunciando no canal ID: {CHANNEL_ID} a cada {INTERVAL_MINUTES} minutos")
    announce.start()

@tasks.loop(minutes=INTERVAL_MINUTES)
async def announce():
    try:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await asyncio.sleep(random.randint(0, 300))  # variação até 5 minutos
            await channel.send(MESSAGE)
            print(f"✅ Mensagem enviada em: {channel.name}")
        else:
            print(f"⚠️ Canal {CHANNEL_ID} não encontrado!")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

bot.run(TOKEN, bot=False)
