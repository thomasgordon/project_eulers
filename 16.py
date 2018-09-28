num = 2 ** 1000
total = 0

for i in range(0, len(str(num))):
    num = str(num)
    temp2 = num[i]

    temp2 = int(temp2)
    total = total + temp2

print(total)
