import messages
import user_data
from errors import WrongSyntax
from errors import RulesAreNotAgreed


def set_money(message, structure):
    target_id = structure[4]
    if messages.get_type(structure, 3) == "int":
        value = structure[3]
    else:
        raise WrongSyntax
    if messages.get_type(structure, 4) == "id":
        reciever = structure[4]
    else:
        raise WrongSyntax
    data = user_data.read(target_id)
    data["money"] = value
    user_data.write(target_id, data)
    return


def show(structure, message):
    if messages.get_type(structure, 2) == "id":
        target_id = structure[2]
        try:
            print(str(user_data.read(target_id)))
            return str(user_data.read(target_id))
        except FileNotFoundError:
            raise RulesAreNotAgreed
    return "User isn't a User"
