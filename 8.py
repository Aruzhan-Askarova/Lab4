def divisible_by_3_and_4(n):
    # Generator to yield numbers divisible by both 3 and 4 in range [0, n]
    for i in range(n+1):  # iterate from 0 to n inclusive
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage:
n = 50
for num in divisible_by_3_and_4(n):
    print(num)
