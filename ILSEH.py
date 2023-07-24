import os
import json
import logging

from webex_bot.commands.echo import EchoCommand
from commands.CSVCommand import CSVCommand
from webex_bot.webex_bot import WebexBot

from webexteamssdk import WebexTeamsAPI, Webhook, WebhookEvent


log = logging.getLogger(__name__)

token = "ZGYzMDczZDctZjA1MC00MWQxLTg2Y2MtZWRiNzc3NjkwZjBkNDFmY2ZmMTEtOWYw_PE93_2dde685a-340f-4e54-9d12-ed962b306bc4"
test_token = "NTg5ZDg2YTAtMWE2Ny00OTgxLThhNTgtYjE3ZmVlODJmNGVhZWNjNDY0ZTQtNTVl_PE93_2dde685a-340f-4e54-9d12-ed962b306bc4"
api = WebexTeamsAPI(token)

# Create a Bot Object
bot = WebexBot(teams_bot_token=token,
               #approved_rooms=['06586d8d-6aad-4201-9a69-0bf9eeb5766e'],
               bot_name="ILSEH",
               include_demo_commands=True)

request = bot.request
log.warning(bot.request)

# Add new commands for the bot to listen out for.
bot.add_command(EchoCommand())
bot.add_command(CSVCommand(request))

# Call `run` for the bot to wait for incoming messages.
bot.run()



