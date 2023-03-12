import logging
from aiogram import Bot, Dispatcher, executor, types
import markups

TOKEN = "6206247538:AAHrVH9AdGJVALrQBPW6htbTpCoUqdN54kk"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет, <b>{message.from_user.first_name}</b>', parse_mode='html',
                           reply_markup=markups.main_menu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Курсы':
        await bot.send_message(message.from_user.id, "Первая часть работает")


@dp.message_handler()
async def bot_help(message: types.Message):
    if message.text == 'Помощь':
        await bot.send_message(message.from_user.id, "Вторая часть работает")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
