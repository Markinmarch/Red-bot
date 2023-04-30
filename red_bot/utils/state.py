from aiogram.dispatcher.filters.state import State, StatesGroup


class AddRecord(StatesGroup):
    direction = State()
    title = State()
    text = State()
    conditions = State()
    first_photo = State()
    second_photo = State()
    third_photo = State()

class AddUser(StatesGroup):
    name = State()
    age = State()
    gender = State()
    phone = State()