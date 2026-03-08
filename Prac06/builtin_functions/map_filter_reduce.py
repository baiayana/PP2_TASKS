# Use map() and filter() on lists
# Aggregate with reduce()

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

squared = list(map(lambda x: x * x, numbers))
print("Squared numbers:", squared)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

sum_all = reduce(lambda a, b: a + b, numbers)
print("Sum of all numbers:", sum_all)