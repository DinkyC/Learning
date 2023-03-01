import math

def standard_dev(lst_2) -> None:
    dev = deviations(mean(lst_2), lst_2)
    sv = samplevar(dev)
    stdv = round(sv_square(sv, lst_2), 3)
    return stdv

def mean(lst_2):
    mn = sum(lst_2) / len(lst_2)
    return mn

def deviations(mn, lst_2):
    dev = [l - mn for l in lst_2]
    return dev

def samplevar(dev):
    dev_squared = [d ** 2 for d in dev]
    total = sum(dev_squared)
    sv = round((total / (len(dev_squared))), 3)
    return sv

def sv_square(sv, lst_2):
    sqr = math.sqrt(sv)
    return sqr



