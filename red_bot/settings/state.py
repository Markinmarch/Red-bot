from aiogram.dispatcher.filters.state import State, StatesGroup


class AddUser(StatesGroup):
    name = State()
    age = State()
    gender = State()
    phone = State()