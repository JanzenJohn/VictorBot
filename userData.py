import pickle
import os.path
import files

def path(id):
    return "data/"+str(id)+".pkl"


def exists(id):
    return os.path.isfile(path(id))


def write(id, userData):
    files.write(path(id), userData)


def read(id):
    if exists(id):
        return files.read(path(id))


def create(id):
    userData = {
        "money": 0,
        "rank": "nobody",
        "wins": 0

    }
    write(id, userData)


def keyExists(id, key, value):
    with open(path(id), "rb")as f:
        userData = pickle.load(f)
        if key in userData.keys():
            return True
        else:
            userData[key] = value
            write(id, userData)
            return False
