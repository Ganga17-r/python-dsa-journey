def add(a, b):
    return a + b

def square(a):
    return a ** 2
def square_sum(a, b):
    result=add(a,b)
    return square(result)
print(square_sum(3, 2))