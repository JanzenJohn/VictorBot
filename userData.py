import pickle
import os.path


def path(id):
    return "data/"+str(id)+".pkl"


def exists(id):
    return os.path.isfile(path(id))


def write(id, userData):
    with open(path(id), "wb")as f:
        pickle.dump(userData, f)
        #Takes userData and dumps it to file


def read(id):
    if exists(id):
        with open(path(id), "rb")as f:
            userData = pickle.load(f)
            return userData


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