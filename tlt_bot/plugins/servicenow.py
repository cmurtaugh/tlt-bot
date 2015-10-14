from slackbot.bot import listen_to


@listen_to('(INC\d+)')
def servicenow(message, incident_id):
    message.reply("Here's the URL! https://harvard.service-now.com/nav_to.do?uri=incident.do?sysparm_query=number=%s" % incident_id)
