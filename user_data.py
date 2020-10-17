import files


def path(id):
    if "<@!" in id:
        id = id.replace("<@!", "").replace(">","")
        return "data/" + id + ".pkl"
    else:
        return "data/"+ id + ".pkl"


def read(id):
    return files.read(path(id))


def write(id, userData):
    print(path(id), userData)
    files.write(path(id), userData)


def create(id):
    standard = {
        "money": 0,
        "rank": 0,
    }
    write(id, standard)


def add_key(id, key, value):
    data = read(id)
    data[key] = value
    write(id, data)
    return
