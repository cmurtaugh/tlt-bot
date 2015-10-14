from slackbot.bot import respond_to
import re


@respond_to('.*', re.IGNORECASE)
def testing(message):
    print message
    message.reply("got it!")
