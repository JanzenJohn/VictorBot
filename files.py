import pickle

def read(file):
    with open(file, "rb")as f:
        output = pickle.load(f)
        return output

def write(file, input):
    with open(file, "wb")as f:
        pickle.dump(input, f)
