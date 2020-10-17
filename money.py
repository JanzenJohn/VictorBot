import user_data
import random
import messages
from datetime import date
from errors import LowerOrEqualZero
from errors import MoneyNotEnough

class AmountLowerEqualZero(Exception):
    pass


class AmountLowerThanMoney(Exception):
    pass


def get(id):
    return int(user_data.read(id)["money"])


def send(sender_id, target_id, amount):
    sender_data = user_data.read(sender_id)
    target_data = user_data.read(target_id)
    if get(sender_id) < amount:
        raise MoneyNotEnough
    else:
        sender_data["money"] = get(sender_id) - amount
        target_data["money"] = get(target_id) + amount
        user_data.write(sender_id,sender_data)
        user_data.write(target_id,target_data)

    return

def daily(id):
    data = user_data.read(id)
    if data["lastDaily"] == str(date.today()):
        return False
    elif data["lastDaily"] != str(date.today()):
        data["money"] = data["money"] + 1000
        data["lastDaily"] = str(date.today())
        user_data.write(id, data)
        return True


def coinflip(amount, id):
    data = user_data.read(id)
    money = get(id)
    amount = int(amount)
    if amount <= 0:
        raise LowerOrEqualZero
    if random.randint(0, 1) == 1:
        data["money"] = money + amount
        user_data.write(id, data)
        return True
    else:
        data["money"] = money - amount
        user_data.write(id, data)
        return False
