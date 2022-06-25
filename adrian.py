import logging
from aiogram import Bot, types, executor, Dispatcher
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as fmt
from aiogram import types
bot = Bot(token='5418995392:AAEJ98Pv1FdTYQKrxd7lhax8Zm0vhIPiCy0')
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    await message.reply("Здравствуйте вас приветсвует поисковой бот,чем могу помочь?")
'''@dp.message_handler(commands="next")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["рынок нефти", "цены на нефть"]
    keyboard.add(*buttons)
    await message.answer("помощь", reply_markup=keyboard)
@dp.message_handler(Text(equals="цены на нефть"))
async def with_puree(message: types.Message):
    await message.reply("ссылка1")
@dp.message_handler(lambda message: message.text == "рынок нефти")
async def without_puree(message: types.Message):
    await message.reply("ссылка2")'''
@dp.message_handler(commands="next")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="BRANT", url="https://ru.investing.com/commodities/brent-oil"),
        types.InlineKeyboardButton(text="Performance", url="https://www.profinance.ru/chart/brent/")
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await message.answer("Кнопки-ссылки", reply_markup=keyboard)

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
    

