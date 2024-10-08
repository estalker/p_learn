import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.filters import Filter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

key = open('token_key.secret', 'r').read()

bot = Bot(token=key)
dp = Dispatcher(storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Рассчитать"), KeyboardButton(text="Информация")]],
    resize_keyboard=True
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)



@dp.message(F.text == "Рассчитать")
async def set_age(message,state):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    cals = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5;
    await message.answer(f"Ваша норма калорий {cals}")
    await state.finish()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
