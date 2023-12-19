from . import account_handlers
from . import post_handlers


TIMEOUT_MESSAGES = {
    'registration': 30,
    'create_post': {
        'title': 60,
        'text': 600,
        'conditions': 300,
        'photo': 120
    },
    'delete_post': 60
}