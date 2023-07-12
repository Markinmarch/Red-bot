from aiogram import types


from red_bot.settings.setting import dp
from red_bot.sql_db.posts import posts
from red_bot.settings.config import CHANNEL_URL


@dp.message_handler(commands = ['my_posts'])
async def checking_posts(message: types.Message):
    '''
    Метод вызывает по команде пользователя список его записей,
    оставленных им на канале.
        :commands: команда, по которой декоратор вызывается
        :message: тип представления данных
    '''
    request_posts_list = posts.select_posts(message.from_user.id)
    ready_posts_list = [num_posts[0] for num_posts in request_posts_list]
    for num_post in ready_posts_list:
        await message.answer(
            text = f'<a href = "{CHANNEL_URL}/{num_post}">{num_post}</a>',
            parse_mode = 'HTML'
        )
    # сформировать кнопки для каждой запси с последующим функционалом - удалить/измнить