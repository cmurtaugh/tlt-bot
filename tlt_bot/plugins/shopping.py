from slackbot.bot import listen_to
import re


@listen_to('shopping', re.IGNORECASE)
def shopping(message):
    message.reply("Don't you mean Course Selection Period?")


@listen_to('shopper', re.IGNORECASE)
def shopper(message):
    message.reply("Ahem. Prospective Enrollee?")


@listen_to('study card', re.IGNORECASE)
def studycard(message):
    message.reply("How about a :crimson_cart:?")
