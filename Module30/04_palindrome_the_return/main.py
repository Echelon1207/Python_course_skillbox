from collections import Counter

def can_be_poly(string):
    my_string = [sym for sym in string.lower() if sym.isalpha()]
    count = Counter(my_string)
    odd_letter = sum(1 for key,val in count.items() if val % 2)
    if odd_letter <= 1:
        return True
    return False

print(can_be_poly('abcba'))
print(can_be_poly('abc'))