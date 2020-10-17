import alias


def main():
    result = "Balance shows your balance. Aliases :"+str(alias.money)+"\n" +\
             "Help lists the help. Aliases :"+str(alias.help) + "\n" + \
             "Coinflip does a coinflip. Aliases :" + str(alias.coinflip) + "\n" + \
             "Daily does a coinflip. Aliases :" + str(alias.daily) + "\n" + \
             "\n" \
             "Bot version ALPHA"
    return result
