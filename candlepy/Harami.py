def Bullish(lastcandle,beforecandle):
    o=float(lastcandle[1])
    h=float(lastcandle[2])
    l=float(lastcandle[3])
    c=float(lastcandle[4])

    o_=float(beforecandle[1])
    h_=float(beforecandle[2])
    l_=float(beforecandle[3])
    c_=float(beforecandle[4])

    return o_ > c_ and c_ < o < c <= o_ and 1.5*(c - o) < (o_ - c_)
    

def Bearish(lastcandle,beforecandle):
    o=float(lastcandle[1])
    h=float(lastcandle[2])
    l=float(lastcandle[3])
    c=float(lastcandle[4])

    o_=float(beforecandle[1])
    h_=float(beforecandle[2])
    l_=float(beforecandle[3])
    c_=float(beforecandle[4])

    return c_ > o_ and o_ < c < o <= c_ and 1.5*(o - c) < (c_ - o_)
