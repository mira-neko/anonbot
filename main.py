from aiogram import Bot, Dispatcher, executor, types
from os import environ
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.INFO)

TOKEN = environ["TOKEN"]
CHANNEL = environ["CHANNEL"]

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f"Бот для анонимного общения в канале {CHANNEL}")

@dp.message_handler()
async def msg(message: types.Message):
    await bot.send_message(CHANNEL, message.text)

logging.info(f"Token: {TOKEN}")
logging.info(f"Channel: {CHANNEL}")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
