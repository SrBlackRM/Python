def ordenate_min_max(Array):
    mins = []
    for i in range(0,4):
        mins.append(min(Array))
        Array.remove(min(Array))
    return mins

def ordenate_max_min(Array):
    maax = []
    for i in range(0,4):
        maax.append(max(Array))
        Array.remove(max(Array))
    return maax