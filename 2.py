x = 1
y = 2
total = 2

while x + y < 4000000:
    z = x + y
    if z % 2 == 0:
        total = total + z
    x = y
    y = z
print(total)
