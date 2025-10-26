from functools import reduce

a = [1, 2, 3]

b = reduce(lambda a, b: a + b, a)
print(b)
