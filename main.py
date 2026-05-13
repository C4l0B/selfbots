import discord
from discord.ext import tasks, commands
import asyncio
import random
import os

# ================= CONFIGURAÇÃO =================
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
INTERVAL_MINUTES = int(os.getenv("INTERVAL_MINUTES", 30))

# Mensagem (você pode editar aqui ou criar variável no Railway)
MESSAGE = os.getenv("MESSAGE", """🚀 **Anúncio do meu produto!**

Olá pessoal! Meu produto está em promoção!
Link: https://seusite.com

Qualquer dúvida é só chamar no PV! 🔥""")

if not TOKEN:
    print("❌ DISCORD_TOKEN não configurado!")
    exit(1)
if not CHANNEL_ID:
    print("❌ CHANNEL_ID não configurado!")
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

bot.run(TOKEN, bot=False)
