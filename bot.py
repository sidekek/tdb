#hello evan
import discord
from enum import Enum

COMMAND_PREFIX = ""

client = discord.Client()

class Style(Enum):
    TEXT = 1                                                                            # plaintext response
    IMAGE_EMBED = 2                                                                     # sends response message as discord embed, with the response parameter as url

class CCommand:
    def __init__(self, strTrigger, strResponse, stlCommandType = Style.TEXT):
        self.strTrigger = strTrigger                                                    # what? why am i allowed to do this?
        self.strResponse = strResponse
        self.stlCommandType = stlCommandType

commands = [                                                                            # a list of commands
    CCommand("testTrigger", "testResponse"),
    CCommand("testEmbed", "https://cdn2.thecatapi.com/images/4ia.gif", stlCommandType = Style.IMAGE_EMBED)
]

@client.event
async def on_message(message):                                                          # triggers on any message received
    if (message.author == client.user): return                                          # filter for messages by the bot
    if (message.type != discord.MessageType.default): return                                    # we only want to process regular messages
    for cmdCommand in commands:                                                         # enumerate through our list of commands
        if (COMMAND_PREFIX + cmdCommand.strTrigger.lower() in message.content.lower()): # if the trigger phrase is in the message,
            if (cmdCommand.stlCommandType == Style.TEXT):                               # and the command type is correct, 
                await message.channel.send(cmdCommand.strResponse)                      # send the appropriate response
            elif (cmdCommand.stlCommandType == Style.IMAGE_EMBED):
                embed = discord.Embed()
                embed.set_image(url=cmdCommand.strResponse)
                await message.channel.send(embed=embed)                                 # send with embed overloaded
            return                                                                      # we don't want to send any more responses to this messages

client.run("YOUR_TOKEN_HERE", bot=True)     # overload false for self/user bots