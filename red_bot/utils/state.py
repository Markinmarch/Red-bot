from aiogram.filters.state import State, StatesGroup


class AddPost(StatesGroup):
    title = State()
    text = State()
    conditions = State()
    photo = State()

class AddUser(StatesGroup):
    phone = State()

class DeletePost(StatesGroup):
    num_post = State()

class MessageToAdmin(StatesGroup):
    message_to_admin = State()