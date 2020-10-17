import user_data
import random
import messages
from datetime import date

class AmountLowerEqualZero(Exception):
    pass


class AmountLowerThanMoney(Exception):
    pass


def get(id):
    return int(user_data.read(id)["money"])


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
    money = int(data["money"])
    amount = int(amount)
    if amount <= 0:
        raise ValueError
    if random.randint(0, 1) == 1:
        data["money"] = money + amount
        user_data.write(id, data)
        return True
    else:
        data["money"] = money - amount
        user_data.write(id, data)
        return False
