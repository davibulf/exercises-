def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


#  print(ack(3, 4))

def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


#  print(is_palindrome("kayak"))


def is_power(a, b):
    if a < b:
        return False
    elif b == 0 or b == 1:
        return False
    elif a % b == 0 or is_power(a/b, b) is True:
        return True
    else:
        return False


#  print(is_power(8, 2))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


#  print(gcd(96, 33030))
