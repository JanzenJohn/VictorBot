import files


async def check_forbidden(message):
    forbidden = files.read("banned.pkl")
    for x in forbidden:
        if x in message.content:
            await reply("Denied : "+x, message)
            return True


async def reply(text, message):
    await message.channel.send(str(text))


def extract_structure(message):
    if message.content[3] == " ":
        return message.content.split()
    else:
        structure = message.content[:3]+" "+message.content[3:]
        return structure.split()


def get_type(structure, digit):
    print(structure)
    try:
        int(structure[digit])
    except ValueError:
        if "<@!" in structure[digit]:
            return "id"
        else:
            raise TypeError
    return "int"
