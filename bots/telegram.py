import logging, sys, os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.brain import Fuffy
from core.safe_executor import execute_command
from core.consts import TELEGRAM_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot)

fuffy = Fuffy()

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.reply("Hello! I am Fuffy, your AI assistant. Tell me what you want to do on your computer.")

@dp.message_handler()
async def handle_message(message: Message):
    user_message = message.text
    try:
        thinking_message = await message.reply("🤔 Thinking...")

        ai_response = fuffy.think(user_message)

        try:
            await thinking_message.delete()
        except Exception as e:
            logging.warning(f"Failed to delete thinking message: {e}")

        await message.reply(ai_response)

        # system_response = execute_command(ai_response)
        # await message.reply(f"{system_response}")

    except Exception as e:
        logging.exception("Error while handling the message")
        await message.reply("An error occurred while processing your request 😢")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)