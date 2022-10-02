number = int(input("Enter number "))
exponent = int(input("Enter Exponent "))
result = 1
ctr = 1

while ctr <= exponent:
    result = result * number
    ctr += 1

print(result)


