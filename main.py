from aiogram import Dispatcher, Bot, filters, types

import asyncio


bot = Bot(token="7056847473:AAEC9SKOCwFxg2Un-6wT0sbvMb9TNregUcQ")
dp = Dispatcher(bot=bot)

@dp.message(commands=["start"])
async def start_function(message: types.Message):
    await message.answer("Salom")

@dp.message(Text="basketball", ignore_case=True)
async def echo_function(message: types.Message):
    await message.answer("1. Kobe \n2. LeBron \n3. Curry")

@dp.message(Text="3")
async def steph_function(message: types.Message):
    await message.answer_photo(photo="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Kobe_Bryant_2014.jpg/640px-Kobe_Bryant_2014.jpg", caption="Stephen Curry - American basketball point guard")

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
