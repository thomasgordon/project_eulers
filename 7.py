from euler import isPrime
x = 0
i = 1

while i <= 10001:
    if isPrime(x):
        x += 1
        i += 1
    else:
        x += 1

print(x)
