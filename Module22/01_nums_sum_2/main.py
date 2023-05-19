file = open('numbers.txt')
nums = file.read()
nums_list = nums.split()
summ = 0
for i in nums_list:
    summ += int(i)
file.close()
new_file = open('answer.txt','w')
new_file.write(str(summ))
