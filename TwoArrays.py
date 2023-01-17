#Given two Arrays in which values are the power of each soldier, return true if you survive the attack or false if you perish.
def is_defended(atks, defs):
    atkPow, defPow = sum(atks),sum(defs)
    survivors = len(defs) - len(atks) + sum((a>b)-(a<b) for a,b in zip(defs,atks))
    return survivors>0 if survivors else defPow>=atkPow
