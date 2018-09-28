x = 0
z = 0

for i in range(1, 101):
    x = x + (i ** 2)
    z = z + i

z = z ** 2
result = z - x

print(result)
