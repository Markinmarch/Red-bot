import os
import logging


from . import bot_tables
from . import posts_db
from . import responders_db
from . import users_db

bot_tables.start_db()

posts = posts_db.Posts()
users = users_db.Users()
responders = responders_db.Responders()
