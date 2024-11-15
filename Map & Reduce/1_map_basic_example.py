numbers = [1, 2, 3, 4]

squares = []
for x in numbers:
    squares.append(x ** 2)

print(squares)

squares = map(lambda n: n ** 2, numbers)

print(list(squares))
