import os
import json
import logging
from dotenv import load_dotenv

from webex_bot.commands.echo import EchoCommand
from commands.CSVHelp import CSVHelpCommand as CSVLocal
from webex_bot.webex_bot import WebexBot

from webexteamssdk import WebexTeamsAPI, Webhook, WebhookEvent


log = logging.getLogger(__name__)
load_dotenv()

# Create a Bot Object
bot = WebexBot(teams_bot_token=os.getenv("WEBEX_TEAMS_ACCESS_TOKEN"),
               #approved_rooms=['06586d8d-6aad-4201-9a69-0bf9eeb5766e'],
               bot_name="ILSEH",
               include_demo_commands=True)

request = bot.request
log.warning(bot.request)

# Add new commands for the bot to listen out for.
bot.add_command(EchoCommand())
bot.add_command(CSVLocal())

# Call `run` for the bot to wait for incoming messages.
bot.run()



