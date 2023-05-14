def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: division by zero"
    else:
        return x / y

print(add(3,4))
print(subtract(8,7))
print(multiply(3,4))
print(divide(8,7))