import discord
import pickle
import messages
import commands
from errors import WrongSyntax


with open("token.pkl", "rb")as f:
    token = pickle.load(f)

victor = discord.Client()


@victor.event
async def on_ready():
    print("login as "+str(victor.user))


@victor.event
async def on_message(message):
    if message.author == victor.user or str(message.author) == "OwO#8456":
        return
    if await messages.check_forbidden(message):
        await message.delete()
        return
    if not message.content.lower().startswith("vic"):
        return
    try:
        await commands.run(message)
    except FileNotFoundError:
        await messages.reply("A file couldn't be read", message)
    except IndexError:
        await messages.reply("Could not access all parameters make sure to use all", message)
    except WrongSyntax:
        await messages.reply("Syntax wrong", message)








victor.run(token)