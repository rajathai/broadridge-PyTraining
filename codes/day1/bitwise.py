# Bitwise Operators in Python

# Bitwise AND (&)
a = 12  # 1100 in binary
b = 15  # 1111 in binary
print("Bitwise AND (a & b):", a & b)  # Result is 1100 in binary which is 12 in decimal

# Bitwise OR (|)
print("Bitwise OR (a | b):", a | b)  # Result is 1111 in binary which is 15 in decimal

# Bitwise XOR (^)
print("Bitwise XOR (a ^ b):", a ^ b)  # Result is 0011 in binary which is 3 in decimal

# Bitwise NOT (~)
print("Bitwise NOT (~a):", ~a)  # Result is -13, which is the two's complement of 12

# Bitwise Left Shift (<<)
print(
    "Bitwise Left Shift (a << 2):", a << 2
)  # Left shift the bits of a by 2, result is 48

# Bitwise Right Shift (>>)
print(
    "Bitwise Right Shift (a >> 2):", a >> 2
)  # Right shift the bits of a by 2, result is 3
