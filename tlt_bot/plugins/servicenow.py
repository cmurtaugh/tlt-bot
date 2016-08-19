from slackbot.bot import listen_to
import re

@listen_to('(INC\d+)')
def servicenow(message, incident_id):
    message.reply("Here's the URL! https://harvard.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=%s" % incident_id)

@listen_to('clos[e|ing]\s.*ticket')
def tickets(message):
    message.reply(":rose2:")
