

def spell_bk(word):
    index = len(word) - 1
    while index < len(word):
        letter = word[index]
        print(letter)
        index = index - 1
        if index == -1:
            break


# spell_bk("banana")


def find(start, word, letter):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return - 1


#   print(find(2, "Corridor", "o"))


def count(wordle, letter):
    c = 0
    for a in wordle:
        if a == letter:
            c = c + 1
    print(c)


#  count("catamaran", "a")

# inp = input("check palindrome:")


def is_palindrome(w):
    if w[0:len(w)] == w[::-1]:
        print("Yes")
    else:
        print("No")


# is_palindrome("tac o cat")


# def rotate_word(word, n):
#     c = 0
#     w = list(word)
#     print(w)
#     while c < len(w) and c != len(w) + 1:
#         letter = w[c]
#         numb_letter = ord(letter) - 97
#         print(numb_letter)
#         if n > 25:        # restart from "A" if exceed alphabet
#             letter = w[c]
#             n_2 = n % 25
#             n_2 = 0 + n_2 - 1
#             print(n_2)
#             le = n_2 + numb_letter
#             if (n_2 + le) > 25:
#                 n_3 = (n_2 + le) - 25
#                 n_3 = 0 + n_3 - 1
#                 el = b[n_3 + numb_letter]
#                 print(el)
#                 new_letter = letter.replace(letter, el)
#                 print(new_letter)
#             else:
#                 el = b[le]
#                 print(el)
#                 new_letter = letter.replace(letter, el)
#                 print(new_letter)
#         else:       # else start from "A"
#             letter = w[c]
#             numb_letter = ord(letter) - 97
#             #  print(numb_letter)
#             el = b[n + numb_letter]
#             new_letter = letter.replace(letter, el)
#             print(new_letter)
#         c = c + 1
#
#
# rotate_word("az", 25)


u = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

p = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

v = [" "]


def rotate_word(word, n):
    c = 0
    w = list(word)
    while c < len(w) and c != len(w) + 1:
        letter = w[c]
        if ord(letter) == 32:
            for i in range(1):
                print(" ", end="")
        elif ord(letter) in range(65, 89):
            numb_letter = ord(letter) - 65
            el = n + numb_letter
            if el > 25:
                el = el % 25
            le = u[el]
            new_letter = letter.replace(letter, le)
            print(new_letter, end="")
        elif ord(letter) == 90:
            numb_letter = 0
            el = n + numb_letter
            if el > 25:
                el = el % 25
            le = u[el]
            new_letter = letter.replace(letter, le)
            print(new_letter, end="")
        elif ord(letter) == 122:
            numb_letter = 0
            el = n + numb_letter
            if el > 25:
                el = el % 25
            le = p[el]
            new_letter = letter.replace(letter, le)
            print(new_letter, end="")
        elif ord(letter) == 90:
            numb_letter = 0
            el = n + numb_letter
            if el > 25:
                el = el % 25
            le = u[el]
            new_letter = letter.replace(letter, le)
            print(new_letter, end="")
        elif ord(letter) == 122:
            numb_letter = 0
            el = n + numb_letter
            if el > 25:
                el = el % 25
            le = p[el]
            new_letter = letter.replace(letter, le)
            print(new_letter, end="")
        else:
            numb_letter = ord(letter) - 97
            el = n + numb_letter
            if el > 25:
                el = el % 25
            le = p[el]
            new_letter = letter.replace(letter, le)
            print(new_letter, end="")
        c = c + 1


print(ord("a"))
inp_1 = input("Insert message:")

rotate_word(inp_1, 1)

