def check_int():
    while True:
        x = input("Please enter a number: ")
        try:
            x = int(x)
            return x
        except ValueError:
            print('Please insert a valid number!')


a = check_int()
b = check_int()
c = check_int()


# check if is a right triangle


def is_triangle(a, b, c):
    if a + b < c or a + c < b or c + b < a:
        print("No")
    else:
        print("Yes")


is_triangle(a, b, c)
