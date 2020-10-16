import pickle

with open("token.pkl", "wb")as f:
    token = "YOUR TOKEN HERE"
    pickle.dump(token, f)