from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import requests


# MANBA : @MistrUZ | @MrGayratov
# API MANBA : @ITMAKTABI1 | @SuppercoderUz
# MANBAGA TEGILMASIN !!!

TOKEN = "5808906937:AAEzddcKvb_QWS6QOy_01IjXHXdRHBfWSfw"
bot = Bot(token=TOKEN, parse_mode='markdown')
orgblacknero = Dispatcher(bot)

channel = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Bizning Kanal",url="https://t.me/uzbdevoloper")]])

@orgblacknero.message_handler(commands=['start'])
async def HGADM(message: types.Message):
    await message.reply(f"*👋Assalamu aleykum {message.from_user.first_name}\n🤖: Men krill-lotin va lotin-krill ga bexato o'girb beraman!  bot creator nero*",reply_markup=channel)

@orgblacknero.message_handler()
async def HGADM(message: types.Message):
    api = requests.get(f"http://supercoders.uz/lotin.php?text={message.text}").json()
    api= (api[0])
    await message.reply(f"{api}")

if __name__ == '__main__':
    executor.start_polling(orgblacknero)