def multiply_all(*args):
    total = 1

    for n in args:
        total = total*n
    return total
print(multiply_all(2, 3, 4))