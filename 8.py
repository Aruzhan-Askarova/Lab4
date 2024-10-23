def squares(a, b):
    # Generator to yield the square of numbers from a to b (inclusive)
    for i in range(a, b+1):
        yield i ** 2

# Example usage:
a = 3
b = 7

for square in squares(a, b):
    print(square)
