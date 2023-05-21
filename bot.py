from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher	
from aiogram import executor

import os

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_set(message: types.Message):
	if message.text == 'Привет':
		await message.answer("Тебе тоже привет!")


executor.start_polling(dp, skip_updates=True)