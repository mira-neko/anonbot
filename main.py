from aiogram import Bot, Dispatcher, executor, types
from os import environ
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.INFO)

TOKEN = environ["TOKEN"]
CHANNEL = environ["CHANNEL"]

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def escape(s):
    for c in "\\.,:;'\"/*-+~`":
        s = s.replace(c, "\\" + c)
    return s

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f"Бот для анонимного общения в канале {CHANNEL}")

@dp.message_handler()
async def msg(message: types.Message):
    if message.text:
        if (CHANNEL[1:] + "/") in message.text.split("\n")[0]:
            text = escape("\n".join(message.text.split("\n")[1:]))
            reply = int(message.text.split("\n")[0].split("/")[-1])
        else:
            text = escape("\n".join(message.text.split("\n")[1:]))
            reply = None
    else:
        text = None
        reply = None
    if message.photo:
        await bot.send_photo(CHANNEL, message.photo, text, "MarkdownV2", reply_to_message_id=reply)
    elif message.text:
        await bot.send_message(CHANNEL, text, "MarkdownV2", reply_to_message_id=reply)
    elif message.sticker:
        await bot.send_sticker(CHANNEL, message.sticker)

logging.info(f"Token: {TOKEN}")
logging.info(f"Channel: {CHANNEL}")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
