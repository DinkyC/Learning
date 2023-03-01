import standard_dev as sd

def zscore(lst):
    z = [((l - sd.mean(lst)) / sd.standard_dev(lst)) for l in lst]
    return z



