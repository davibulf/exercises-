import math


def square_root(a):
    epsilon = 0.00001
    x = a - 1
    while x > epsilon:
        y = (x + a/x) / 2
        if abs(a) < epsilon:
            pass
        elif x == y:
            return x
        else:
            x = y


#  print(type(square_root(64)))


def check_square_root(a):
    for i in range(a - 1):
        b = math.sqrt(a)
        k = abs(square_root(a))
        z = abs(b - k)
        print(a, end=" ")
        print(b, end=" ")
        print(k, end=" ")
        print(z, end=" ")
        print(end="\n")
        a = a - 1

    print("1", end=" ")
    print("1", end=" ")
    print("1", end=" ")
    print("0", end=" ")
    print(end="\n")


#  check_square_root(420)

inp = input("Write expression:")


def calculator():
    while True:
        if inp[len(inp)-1].isdigit():
            print(eval(inp))
            break
        # elif inp == "end":
        #     print("Shutting down")
        #     break
        else:
            print("Please insert operators and digits!")
            break


calculator()
