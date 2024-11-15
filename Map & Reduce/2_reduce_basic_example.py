from functools import reduce

numbers = [1, 2, 3, 4]

res = numbers[0]
for n in numbers[1:]:
    res += n

print(res)

res = reduce(lambda x, y: x + y, numbers)
print(res)