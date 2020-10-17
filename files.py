import pickle
import os

def write(file, data):
    with open(file, "wb")as f:
        pickle.dump(data, f)
    f.close()


def read(file):
    with open(file, "rb")as f:
        return pickle.load(f)
