from slackbot.bot import listen_to
import re
from random import randint


@listen_to('shopping', re.IGNORECASE)
def shopping(message):
    if randint(1, 10) == 5:
        message.reply("Don't you mean Course Selection Period?")


@listen_to('shopper', re.IGNORECASE)
def shopper(message):
    if randint(1, 10) == 5:
        message.reply("Ahem. Prospective Enrollee?")


@listen_to('study card', re.IGNORECASE)
def studycard(message):
    if randint(1, 10) == 5:
        message.reply("How about a :crimson_cart:?")
