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
    if message.text:
        if (CHANNEL[1:] + "/") in message.text.split("\n")[0]:
            await bot.send_message(CHANNEL, "\n".join(message.text.split("\n")[1:]),
                "MarkdownV2", reply_to_message_id=int(message.text.split("\n")[0].split("/")[-1]))
        else:
            await bot.send_message(CHANNEL, message.text, "MarkdownV2")
    if message.sticker:
        await bot.send_sticker(CHANNEL, str(message.sticker))

logging.info(f"Token: {TOKEN}")
logging.info(f"Channel: {CHANNEL}")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
