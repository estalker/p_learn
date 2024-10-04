import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

key = open('token_key.secret','r').read()

bot = Bot(token=key)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    #await message.answer("Привет! Я бот помогающий твоему здоровью.")
    print("Привет! Я бот помогающий твоему здоровью.")

@dp.message()
async def all_massages(message: types.Message):
    #await message.reply("Введите команду /start, чтобы начать общение.")
    print("Введите команду /start, чтобы начать общение.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
