from aiogram.dispatcher.filters.state import State, StatesGroup


class AddAds(StatesGroup):
    title = State()
    text = State()
    conditions = State()
    price = State()

class AddUser(StatesGroup):
    name = State()
    age = State()
    gender = State()
    phone = State()