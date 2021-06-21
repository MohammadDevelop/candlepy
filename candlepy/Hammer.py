def isGreenHammer(cand):
    o=float(cand[1])
    h=float(cand[2])
    l=float(cand[3])
    c=float(cand[4])
    return ( (10*h-10*c)<(o-l) and c>o and (2*c-2*o)<(o-l) )

def isRedHammer(cand):
    o=float(cand[1])
    h=float(cand[2])
    l=float(cand[3])
    c=float(cand[4])
    return ( (10*h-10*o)<(c-l) and o>c and (2*o-2*c)<(c-l) )
    
    
def isGreenHammerInverted(cand):
    o=float(cand[1])
    h=float(cand[2])
    l=float(cand[3])
    c=float(cand[4])
    return ( (10*o-10*l)<(h-c) and c>o and (2*c-2*o)<(h-c) )
    
def isGreenHammerInverted(cand):
    o=float(cand[1])
    h=float(cand[2])
    l=float(cand[3])
    c=float(cand[4])
    return ( (10*o-10*l)<(h-c) and c>o and (2*c-2*o)<(h-c) )


def isRedHammerInverted(cand):
    o=float(cand[1])
    h=float(cand[2])
    l=float(cand[3])
    c=float(cand[4])
    return ( (10*c-10*l)<(h-o) and o>c and (2*c-2*c)<(h-o) )

