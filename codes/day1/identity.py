# Identity Operators in Python

# 'is' and 'is not' operators

# is: Evaluates to True if the variables on either side of the operator point to the same object # Noqa
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print("x is z:", x is z)
print("x is y:", x is y)
print("x == y:", x == y)

# is not: Evaluates to True if the variables on either side of the operator do not point to the same object # Noqa
print("x is not y:", x is not y)
