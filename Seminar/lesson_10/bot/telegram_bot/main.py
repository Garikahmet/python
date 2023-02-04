from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import aiohttp
import time


API_TOKEN = '5934978129:AAHd39un162wbhBYgfu2slolZzu-fmHT21A'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
   user_id = message.from_user.id
   user_name = message.from_user.first_name
   user_full_name = message.from_user.full_name
   await message.reply(f"Hi, {user_full_name}!")
   time.sleep(1)
   btns = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
   btn1 = types.KeyboardButton('/Покажи мне собаку'),
   btn2 = types.KeyboardButton('/Покажи мне кота')
   btns.add(btn1, btn2)
   await bot.send_message(user_id, reply_markup=btns)

@dp.message_handler(commands=['Покажи мне собаку']) 
async def btn1_handler(message): 
   with open("Seminar\lesson_10\bot\telegram_bot\собака.webp", "rb") as f:
      await bot.send_photo(message.chat.id, photo=f)

@dp.message_handler(commands=['Покажи мне кота'])
async def btn2_handler(message):
   with open("Seminar\lesson_10\bot\telegram_bot\кот.jpg, 'rb") as f2:
      await bot.send_photo(message.chat.id, photo=f2)

if __name__ == '__main__':
   executor.start_polling(dp)