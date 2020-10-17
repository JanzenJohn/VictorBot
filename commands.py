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
from errors import LowerOrEqualZero


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

        return
    elif command in alias.send:
        sender_id = "<@!"+str(id)+">"
        reciever_id = structure[3]
        amount = int(structure[2])
        if sender_id == reciever_id:
            await messages.reply("No "+user+", you can't send yourself money", message)
        if amount <= 0:
            raise WrongSyntax
        else:
            print(str(amount)+ "!= 0")
        try:
            money.send(sender_id, reciever_id, amount)
        except money.MoneyNotEnough:
            await messages.reply("No "+user+", you do not have enough money")

    elif command in alias.coinflip:
        try:
            messages.get_type(structure, 2)
            amount = structure[2]
        except TypeError:
            if structure[2] == "all":
                amount = money.get(id)
            else:
                amount = 1
        try:
            print(amount)
            if money.coinflip(amount, id):
                await messages.reply(user+", you got "+'{:,}'.format(int(amount))+"€ !", message)
            else:
                await messages.reply(user+", you lost "+'{:,}'.format(int(amount))+"€ !", message)
        except LowerOrEqualZero:
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

    else:
        await messages.reply(user+", command "+command+" wasn't recognized.", message)



