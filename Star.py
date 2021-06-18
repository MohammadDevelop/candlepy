def MorningStar(lastcandle,beforecandle,thirdlast):
    o1=float(lastcandle[1])
    h1=float(lastcandle[2])
    l1=float(lastcandle[3])
    c1=float(lastcandle[4])

    o2=float(beforecandle[1])
    h2=float(beforecandle[2])
    l2=float(beforecandle[3])
    c2=float(beforecandle[4])


    o3=float(thirdlast[1])
    h3=float(thirdlast[2])
    l3=float(thirdlast[3])
    c3=float(thirdlast[4])

    return l3 < c3 < o3 < h3 and l1 <= o1 < c1 < h1 and abs(o2 - c2) < abs(o3 - c3) and abs(o2 - c2) < abs(o1 - c1) and max(o2,c2) < c3 and max(o2,c2) < o1 

def EveningStar(lastcandle,beforecandle,thirdlast):
    o1=float(lastcandle[1])
    h1=float(lastcandle[2])
    l1=float(lastcandle[3])
    c1=float(lastcandle[4])

    o2=float(beforecandle[1])
    h2=float(beforecandle[2])
    l2=float(beforecandle[3])
    c2=float(beforecandle[4])


    o3=float(thirdlast[1])
    h3=float(thirdlast[2])
    l3=float(thirdlast[3])
    c3=float(thirdlast[4])

    return l3 < o3 < c3 < h3 and l1 <= c1 < o1 < h1 and abs(o2 - c2) < abs(o3 - c3) and abs(o2 - c2) < abs(o1 - c1) and min(o2,c2) > c3 and min(o2,c2) > o1 
