import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

from brain import Fuffy
from safe_executor import execute_command

from consts import TELEGRAM_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

fuffy = Fuffy()

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.reply("Привет! Напиши, что нужно сделать на компьютере.")

@dp.message_handler()
async def handle_message(message: Message):
    user_input = message.text
    ai_response = fuffy.think(f"Ты — помощник, который на вход получает фразу от пользователя, а на выходе возвращает только команду для выполнения в ОС.\n\nФраза: {user_input}\nКоманда:")

    system_response = execute_command(ai_response)

    await message.reply(f"🧠 ИИ сгенерировал:\n`{ai_response}`\n\n{system_response}", parse_mode="Markdown")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)