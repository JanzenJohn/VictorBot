import messages
import files
import money
import user_data
import alias
import admin
import help
from permission import check
from errors import WrongSyntax
from errors import RulesAreNotAgreed


async def run(message):
    try:
        structure = messages.extract_structure(message)
    except IndexError:
        return

    command = structure[1].lower()
    id = str(message.author.id)
    user = "**"+str(message.author)+"**"

    if command in alias.help:
        await messages.reply(help.main(), message)
        return
    elif command in alias.daily:
        try:
            if money.daily(id):
                await messages.reply(user+", here is your daily 1000€", message)
            else:
                await messages.reply(user+", you already got your daily 1000€", message)

        except KeyError:
            user_data.add_key(id, "lastDaily", " ")

    elif command in alias.coinflip:
        try:
            type = messages.get_type(structure, 2)
        except TypeError:
            if structure[2] == "all":
                amount = user_data.read(id)["money"]
            else:
                amount = 1
            type = "all"
        if type == "int":
            amount = structure[2]
        try:
            await messages.reply(money.coinflip(amount, id), message)
        except ValueError:
            await messages.reply(user + ", Nien",message)



    elif command in alias.money:
        await messages.reply(user + ", you have " + '{:,}'.format(money.get(id))+"€", message)
        return

    elif command == "agree":
        user_data.create(id)
        await messages.reply("Okay "+user+" !", message)
        return

    elif command == "set":
        subcommand = structure[2]
        if check(id):
            if subcommand in alias.money:
                admin.set_money(message, structure)
            else:
                raise WrongSyntax
        else:
            await messages.reply(user+" you aren't on the admin list", message)

    elif command == "show":
        try:
            await messages.reply(admin.show(structure, message),message)
        except RulesAreNotAgreed:
            await messages.reply("The user hasn't agreed rules", message)



