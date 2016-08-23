from slackbot.bot import listen_to
import re


@listen_to('(TLT-\d+)', re.IGNORECASE)
def jira(message, ticket):
    message.reply("Here's the URL! https://jira.huit.harvard.edu/browse/%s" % ticket)
