import array as arr

numbers = arr.array('i', [12, 10, 1, 12, 13])

# print array values
ctr = 0
while ctr < len(numbers):
    print(numbers[ctr])
    ctr += 1
print("Loop Done")

