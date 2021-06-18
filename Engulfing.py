def EngulfingCheck(lastcandle,beforecandle):
    o=float(lastcandle[1])
    h=float(lastcandle[2])
    l=float(lastcandle[3])
    c=float(lastcandle[4])

    o_=float(beforecandle[1])
    h_=float(beforecandle[2])
    l_=float(beforecandle[3])
    c_=float(beforecandle[4])

    if(o>c and o_<c_ and o>c_ and o_>c) :
        return -1

    if(o<c and o_>c_ and c>o_ and c_>o) :
        return 1

    return 0
