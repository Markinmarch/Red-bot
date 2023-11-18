from aiogram.filters.state import State, StatesGroup


class AddPost(StatesGroup):
    title = State()
    text = State()
    conditions = State()
    photo = State()

class AddUser(StatesGroup):
    name = State()
    age = State()
    gender = State()
    phone = State()

class DeletePost(StatesGroup):
    num_post = State()