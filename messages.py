import pickle
import once


async def reply(message, text):
    await message.channel.send(str(text))


def extractStructure(message):
    if message.content[0:3].lower() == "vic":
        if message.content[3] != " ":
            temp = message.content[:3] + " " + message.content[3:]
            command = temp.split()
        else:
            command = message.content.split()
        return command


def extractCommand(structure):
    return structure[1].lower()


async def checkForbidden(message):
    with open("banned.pkl", "rb")as f:
        bannedSymbols = pickle.load(f)
    for symbol in bannedSymbols:
        if symbol in message.content:
            await reply(message, "Nein **" + str(message.author) + "**, : " + symbol + " wird hier nicht benutzt")
            return True
    return False


def isAdmin(message):
    if str(message.author) == "KAPITÄN JOHANNES#0001":
        return True
    else:
        return False


async def unban(message):
    bannedSymbols = list()
    text = message.content
    with open("banned.pkl", "rb")as f:
        bannedSymbols = pickle.load(f)
        for x in range(len(text)):
            bannedSymbols.remove(text[x])
        once.dump(bannedSymbols)



async def dump(text):
    bannedSymbols = list()
    print(text)
    with open("banned.pkl", "rb")as f:
        bannedSymbols = pickle.load(f)
        for x in range(len(text)):
            if text[x] in bannedSymbols:
                print(text[x] + " ist schon gedumpt")
                print(bannedSymbols)
            else:
                bannedSymbols = bannedSymbols + list(text[x])
                print(text[x] + " was dumped")
                once.dump(bannedSymbols)


