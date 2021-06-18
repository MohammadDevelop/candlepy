def ThreeWhiteSoldiers(lastcandle,beforecandle,thirdlast):
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

    return o1<c1 and o2<c2 and o3<c3 and  c3<o2<c3 and o2<o1<c2

def ThreeBlackCrows(lastcandle,beforecandle,thirdlast):
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

    return o1>c1 and o2>c2 and o3>c3 and  c3>o2>c3 and o2>o1>c2 
