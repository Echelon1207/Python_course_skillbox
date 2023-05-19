def slicer(text, num):
    count = text.count(num)
    if num not in text:
        new_tuple = tuple()
        return new_tuple
    else:
        index = text.index(num)
        rindex = max(i for i, val in enumerate(text) if val == 2)
        if count >= 2:
            new = text[index:rindex]
            return new
        elif count == 1:
            new = text[index:]
            return new


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 2))
print(slicer((1, 3, 4, 5, 6, 7, 8, 9, 10), 2))
