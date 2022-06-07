def fact1(x):
    result = 1
    for x in range(1, x + 1):
        result = result * x

    return result


def fact2(x):
    result = 1
    while x > 0:
        result *= x
        x -= 1
    return result


def fact3(x):
    result = 1
    for y in range(x, 0, -1):
        result = result * y

    return result


number = input("Test first function: ")
print(fact1(int(number)))

number = input("Test second function: ")
print(fact2(int(number)))

number = input("Test third function: ")
print(fact3(int(number)))
