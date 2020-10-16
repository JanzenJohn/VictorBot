import userData
import discord
import messages
import pickle

victor = discord.Client()

@victor.event
async def on_ready():
    print("login as "+str(victor.user))


@victor.event
async def on_message(message):
    if message.author == victor.user or str(message.author) == "OwO#8456":
        return
    await messages.dump(message.content)






victor.run("NzY2MzI3ODMwODM3NDYxMDQy.X4hwaA.nWh5u02ZxGDKFihSgwi2JCkCL-Y")