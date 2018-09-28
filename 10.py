from euler import isPrime

x = 0
i = 0

for x in range(1, 2000001):
    if isPrime(x):
        i += x
        x += 1
    else:
        x += 1
print(i)
