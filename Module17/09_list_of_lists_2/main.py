from itertools import chain

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
list1 = list(chain(*nice_list))
list2 = list(chain(*list1))

print(list2)    