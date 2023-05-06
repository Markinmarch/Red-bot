from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

class AddPost(StatesGroup):
    direction = State()
    title = State()
    text = State()
    conditions = State()
    photo = State()

class AddUser(StatesGroup):
    name = State()
    age = State()
    gender = State()
    phone = State()
