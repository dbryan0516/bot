import gdax as api


def calcPercentChange(oldPrice, newPrice, feePercentage):
    percent = newPrice / oldPrice - 1
    if (percent > 0):
        # positive increase since last getPrice
        percent = percent - fee
    else:
        # positive increase since last getPrice
        pass
    return percent


def calcFeePercentage(newPrice):
    # TODO: possibly include this in api file
    feePercentage = 0
    return feePercentage


def run():
    while true:
        pass
