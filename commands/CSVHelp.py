import logging

from webexteamssdk.models.cards import Colors, TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, \
    Text, Image, HorizontalAlignment
from webexteamssdk.models.cards.actions import Submit

from webex_bot.formatting import quote_info
from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card

log = logging.getLogger(__name__)


class CSVHelpCommand(Command):

    def __init__(self):
        super().__init__(
            command_keyword="csv",
            help_message="Reads a csv file",
            chained_commands=[CSVCallback()])
            

    def pre_execute(self, message, attachment_actions, activity):
        """
        (optional function).
        Reply before running the execute function.

        Useful to indicate the bot is handling it if it is a long running task.

        :return: a string or Response object (or a list of either). Use Response if you want to return another card.
        """

        image = Image(url="https://media.discordapp.net/attachments/521496346839220224/1132169645055553568/RDT_20230703_2226178576265681859042128.png")
        text1 = TextBlock("Hey there! Please upload a .csv file", weight=FontWeight.BOLDER, wrap=True, size=FontSize.DEFAULT,
                          horizontalAlignment=HorizontalAlignment.CENTER, color=Colors.DARK)
        text2 = TextBlock("Please use the integrated Webex Attachment button to send me a .csv file. Don't forget to @ me if this is a shared group space ;)",
                          wrap=True, color=Colors.DARK)
        card = AdaptiveCard(
            body=[ColumnSet(columns=[Column(items=[image], width=2)]),
                  ColumnSet(columns=[Column(items=[text1, text2])]),
                  ])

        return response_from_adaptive_card(card)

    def execute(self, message, attachment_actions, activity):
        """
        If you want to respond to a submit operation on the card, you
        would write code here!

        You can return text string here or even another card (Response).

        This sample command function simply echos back the sent message.

        :param message: message with command already stripped
        :param attachment_actions: attachment_actions object
        :param activity: activity object

        :return: a string or Response object (or a list of either). Use Response if you want to return another card.
        """

class CSVCallback(Command):

    def __init__(self):
        super().__init__(
            card_callback_keyword="csvHelp_callback",
            delete_previous_message=True)

    def execute(self, message, attachment_actions, activity):
        return quote_info(attachment_actions.inputs.get("message_typed"))
