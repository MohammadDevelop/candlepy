def SpinningTop(lastcandle):
    o=float(lastcandle[1])
    h=float(lastcandle[2])
    l=float(lastcandle[3])
    c=float(lastcandle[4])

    if(c>o and h==c and l==o) :
        return 1

    if(o>c and h==o and l==c) :
        return -1

    return 0
