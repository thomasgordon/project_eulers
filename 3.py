import math
import euler
i = 1

target = 600851475143
max = math.sqrt(600851475143)
value = 0

while i < max:
    if target % i == 0 and euler.isPrime(i):
        if i > value:
            value = i
    i += 1
print(value)
