def even_numbers(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
even_nums = list(even_numbers(n))
print(", ".join(map(str, even_nums)))