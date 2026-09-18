def double(a):
    return a * 2

def square(a):
    return a ** 2

def double_square(a):
    result = square(a)
    return double(result)

print(double_square(5))