
def flat_list(summ):
    if summ == []:
        return summ
    else:
        if isinstance(summ[0], list):
            return flat_list(summ[0]) + flat_list(summ[1:])
        return summ[:1] + flat_list(summ[1:])

def summ_list():
    count = 0
    for i in flat_list(summ):
        count += i
    return count

summ = ([[1, 2, [3]], [1], 3])

print(summ_list())


