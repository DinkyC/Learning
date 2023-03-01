import standard_dev as sd

def zscore_list(lst):
    z = [((l - sd.mean(lst)) / sd.standard_dev(lst)) for l in lst]
    return z


def zscore(data, mean, standard):
    z = ((data - mean) / standard)
    return z