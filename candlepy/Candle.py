#Main General Uilities

def isRED(candle):
    """
    Takes a list of float/string as a candle. NOHLC format (ID,Open,High,Low,Close).
    returns true if it is RED!
    """
    o=float(candle[1])
    c=float(candle[4])
    return o>c

def isGREEEN(candle):
    """
    Takes a list of float/string as a candle. NOHLC format (ID,Open,High,Low,Close).
    returns true if it is GREEN!
    """
    o=float(candle[1])
    c=float(candle[4])
    return o<c

def Trend(candles,count):

    """
    Takes a list of candle sticks and determines its total trend.
    -1 for Descending
    +1 for Ascending
    0 for Neutral
    """

    r=0
    g=0
    for cnd in candles[-1*count:]:
        if isRED(cnd):
            r=r+1
        else:
            g=g+1
    if(r>2*g):
        return -1
    if(g>3*r):
        return 1
    return 0


def inDownTrend(candles,count):
    start=float(candles[len(candles)-count-1][1])
    end=float(candles[len(candles)-1][4])
    return (end<start)

def inUpTrend(candles,count):
    start=float(candles[len(candles)-count-1][1])
    end=float(candles[len(candles)-1][4])
    return (end>start)


# TODO: complete this function
def RedInRow(candles):
    r=0
    i=len(candles)-1
    for cnd in candles[-1*count:]:
        if isRED(cnd):
            r=r+1
        else:
            g=g+1
    if(r>2*g):
        return -1
    if(g>2*r):
        return 1
    return 0
