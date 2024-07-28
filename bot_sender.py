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

message_thread_id = 5
# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
    
def send_message(message):
    bot = Bot(token=BOT_TOKEN)
    try:
        asyncio.run(bot.send_message(chat_id=CHANNEL_ID, text=message,message_thread_id=message_thread_id))
        logger.info("Message sent successfully")
    except TelegramError as e:
        logger.error(f"Failed to send message: {e}")
        