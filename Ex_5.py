# ex_3-3


def eight_justify(s):
    m = " "
    print(m*70, end="")
    print(s)


eight_justify("allen")

# ex_3-4


def do_twice(f, g):
    f(g)
    f(g)


def print_spam():
    print("spam", end="")


def print_twice(k):
    print(k)
    print(k)


do_twice(print_twice, "spam")
