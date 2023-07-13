import os

from webex_bot.commands.echo import EchoCommand
from webex_bot.webex_bot import WebexBot

# Create a Bot Object
bot = WebexBot(teams_bot_token="ZGYzMDczZDctZjA1MC00MWQxLTg2Y2MtZWRiNzc3NjkwZjBkNDFmY2ZmMTEtOWYw_PE93_2dde685a-340f-4e54-9d12-ed962b306bc4",
               #approved_rooms=['06586d8d-6aad-4201-9a69-0bf9eeb5766e'],
               bot_name="ILSEH",
               include_demo_commands=True)

# Add new commands for the bot to listen out for.
bot.add_command(EchoCommand())

# Call `run` for the bot to wait for incoming messages.
bot.run()