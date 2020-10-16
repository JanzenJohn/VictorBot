import pickle

def dump(list):
    with open("banned.pkl", "wb")as f:
        pickle.dump(list, f)

