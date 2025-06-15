import os
from telegram import Bot
from telegram.ext import Updater
from keep_alive import keep_alive

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
MIN_USD = int(os.getenv("MIN_USD", 5000))

bot = Bot(token=BOT_TOKEN)

def start_bot():
    print("Bot iniciado...")
    print(f"Enviando alertas a: {CHANNEL_USERNAME}")
    # Aquí podrías conectar con Binance o cualquier fuente de datos

if __name__ == "__main__":
    keep_alive()
    start_bot()