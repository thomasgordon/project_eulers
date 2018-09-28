num = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        z = x * y
        string = str(z)
        if string == string[::-1] and z > num:
            num = z
print(num)
