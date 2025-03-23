def power(a, b):
    result = 1
    base = a  # First extra variable
    exponent = b  # Second extra variable

    while exponent > 0:
        result *= base
        exponent -= 1

    return result


# Example usage
a = 3
b = 4
print(power(a, b))  # Output: 81 (3^4 = 81)
