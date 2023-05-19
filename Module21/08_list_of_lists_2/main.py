
def flat_list(nice_list):
    if nice_list == []:
        return nice_list
    else:
        if isinstance(nice_list[0], list):
            return flat_list(nice_list[0]) + flat_list(nice_list[1:])
        return nice_list[:1] + flat_list(nice_list[1:])


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(flat_list(nice_list))