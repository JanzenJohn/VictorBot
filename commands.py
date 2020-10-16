import userData
import messages
import random
import datetime

async def run(command, message, structure):
    if command == "userdata":
        if userData.exists(message.author.id):
            await messages.reply(message, str(userData))
    if command == "setup":
        if userData.exists(message.author.id):
            await messages.reply(message, "UserData for **"+str(message.author)+"** already exists")
        else:
            userData.create(message.author.id)
        return
    if command == "cash":
        if userData.exists(message.author.id):
            await messages.reply(message, "**"+str(message.author)+"**, you currently have "+'{:,}'.format(userData.read(message.author.id)["money"])+"€")
        else:
            await run("setup",message,structure)
            await run(command,message,structure)
    if command == "cf" or command == "coinflip":
        if userData.exists(message.author.id):
            try:
                bet = structure[2]
            except IndexError:
                bet = 1
            try:
                bet = int(bet)
            except ValueError:
                if bet == "all":
                    bet = userData.read(message.author.id) ["money"]
                else:
                    bet = 1
            if userData.read(message.author.id)["money"] < bet:
                await messages.reply(message, "You dont have enough money")
                return
            if bet <= 0:
                await messages.reply(message, "HABEN SIE NICHT VERSTANDEN WIE FUNKTIONIERT ?")
                return
            data = userData.read(message.author.id)
            if random.randint(0,1) == 1:
                await messages.reply(message, "**"+str(message.author)+"**,"+" you have won : "+'{:,}'.format(bet)+"€")
                data["money"] = data["money"] + bet
                userData.write(message.author.id, data)
                return
            else:
                await messages.reply(message,"**"+str(message.author)+"**,"+" you have lost : "'{:,}'.format(bet)+"€")
                data["money"] = data["money"] - bet
                userData.write(message.author.id, data)
                return
        else:
            await run("setup", message, structure)
            await run("cf", message, structure)

    if command == "daily":
        if userData.exists(message.author.id):
            if not userData.keyExists(message.author.id,"lastDaily",str(datetime.date.today())):
                await messages.reply(message, "You got 1,000 €")
                data = userData.read(message.author.id)
                data["money"] = data["money"]+1000
                userData.write(message.author.id, data)
                return
            elif userData.read(message.author.id)["lastDaily"] == str(datetime.date.today()):
                await messages.reply(message, "You have already claimed your daily")

        else:
            await run("setup", message, structure)
            await run(command,message,structure)

