

logFile = open("transactions.log", "a")


def log(message):
    logFile.write(message)


# Selling Logger
def logSell(coinType, coinAmt, buyPrice, sellPrice, percentDiff, extraInfo):
    message = ""
    if (percentDiff > 0):
        message = "GAIN: "
    else:
        message = "LOSS: "

    message += "Sold: " + str(coinAmt) + coinType + " at Price: $" +  \
               str(sellPrice) + " Bought at Price: $" + str(buyPrice) + \
        " Percent Diff: %" + str(percentDiff * 100)

    if (extraInfo):
        message += "EXTRA: " + extraInfo

    log(message + "\n")

# Buy logger


def logBuy(coinType, coinAmt, costTotal, costPer, extraInfo):
    message = "\t"
    message += "BOUGHT: " + str(coinAmt) + coinType + \
        " For: $" + str(costTotal) + " at $" + str(costPer) + "/Coin"
    if (extraInfo):
        message += "EXTRA: " + extraInfo
    log(message + "\n")


logSell("LTC", 1.5789031, 54.55, 57.88, .02, None)
logBuy("LTC", 1.34567, 60, 45, None)
