import asyncio
import logging
import os
from telegram import Update,Bot
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram.error import TelegramError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the bot token and channel ID from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
message_thread_id = 5  # Only needed if you want to send to a specific topic in a group, otherwise dont send it to bot.send_message.py


  
def send_message(message):
    bot = Bot(token=BOT_TOKEN)
    try:
        asyncio.run(bot.send_message(chat_id=CHANNEL_ID, text=message,message_thread_id=message_thread_id))
    except TelegramError as e:
        print(f'Error sending message\n {e.message}')        