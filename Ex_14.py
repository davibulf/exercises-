from random import *
# eng2sp = dict()
# eng2sp["one"] = "uno"
# eng2sp["two"] = "dos"
# eng2sp["three"] = "tres"
# print(eng2sp)
# print(eng2sp["two"])
# print(len(eng2sp))
# vals = eng2sp.values()
# print("uno" in vals)

f = open('../txt/word.txt')


def create_word_dict(x):
    word_dict = dict()
    for line in x:
        word = line.strip()
        word_dict[word] = randint(1, 100)
    return word_dict


# print(create_word_dict(f))


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


# print(histogram("brontosaurus"))


def reverse_lookup(d, v):
    li = list()
    for c in d:
        if d[c] == v:
            li.append(c)
    return li


# h = histogram("parrot")
# k = reverse_lookup(h, 1)
# print(k)


def invert_dict(d):
    inverse = {}
    for key in d:
        new_key = d[key]
        value = inverse.setdefault(new_key, [])
        value.append(key)
    return inverse


o = {"a": 4, "b": 3, "c": 3, "e": 5}
print(invert_dict(o))

