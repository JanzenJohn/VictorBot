import discord
import messages
import commands
import pickle


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
    if await messages.checkForbidden(message):
        await message.delete()
        return
    if not message.content.startswith("vic"):
        return
    structure = messages.extractStructure(message)
    command = messages.extractCommand(structure)
    await commands.run(command, message, structure)







victor.run(token)