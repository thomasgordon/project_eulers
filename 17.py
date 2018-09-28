import inflect

p = inflect.engine()
nums = []
words = []
total = 0

for x in range(1, 1001):
    nums.append(x)

for y in range(0, len(nums)):
    temp1 = p.number_to_words(nums[y])
    print(temp1)
    words.append(temp1)

words.replace('-', '')

s = ''
s = s.join(words)

print(s)
