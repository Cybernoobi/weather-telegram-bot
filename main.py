from weather.main import get_weather
from aiogram import Dispatcher, Bot, types, executor
from config import TGAPI


bot = Bot(TGAPI)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(messge: types.Message):
    await messge.reply(text='Привет, если нужна помощь пищи /help')

@dp.message_handler(commands=['help'])
async def help(messge: types.Message):
    await messge.reply(text='Привет, напиши любой город о котором хочешь узнать погоду')

@dp.message_handler()
async def wetherstart(message: types.Message):
    try:
        weatherinfo = get_weather(message.text)
        await message.reply(text=weatherinfo)
    except Exception:
        await message.reply(text='Город не найден')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)