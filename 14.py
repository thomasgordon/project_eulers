import time

longestLen = 0
longestNum = 0
x = 0
startTime = time.time()

for i in range(1, 1000000):
    n = i
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            x += 1
        else:
            n = (3 * n) + 1
            x += 1
    if x > longestLen:
        longestLen = x
        longestNum = i
print("Took", (time.time() - startTime))
print("Result is:", longestNum)
