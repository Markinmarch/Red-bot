from aiogram import types, F


from ...settings.setting import dp
from ..keyboards.reply_keyboard import by_agreement, title_detection_buttons
from ..state import AddPost
from ..content.text_content import FILTERS_MESSAGE

    
# Фильтр, который требует от пользователя ввести не менее 20 символов для описания
@dp.message(
    AddPost.text,
    F.text.len() < 20
)
async def repeat_enter_text(message: types.Message):
    await message.answer(text = FILTERS_MESSAGE['create_post']['repeat_text'])

# Фильтр, который указывает пользователю, что необходимо в условиях указывать цену (в цифрах)
@dp.message(
    AddPost.conditions,
    ~F.text == int or ~F.text == 'По договорённости'
)
async def repeat_enter_condition(message: types.Message):
    await message.answer(
        text = FILTERS_MESSAGE['create_post']['repeat_condition'],
        reply_markup = by_agreement
    )

# Фильтр, который позволяет выбрать тему только из предложенных вариантов на клавиатуре
@dp.message(
    AddPost.title,
    ~F.text.in_([button.text for button in title_detection_buttons.keyboard[0]]),
)
async def repeat_enter_title(message: types.Message):
    await message.answer(
        text = FILTERS_MESSAGE['create_post']['repeat_title'],
        reply_markup = title_detection_buttons
    )
