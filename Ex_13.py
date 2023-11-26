import time
a = [2, 3, [5, 6, 7], [8, 9], 10]


def nested_sum(m):
    b = m[2]
    c = m[3]
    d = b + c
    print(sum(d))


#   nested_sum(a)

p = [1, 2, 3, 4, 5, 6]


def middle(m):
    del m[1:(len(m)-1)]
    print(m)


#   middle(p)


def chop(m):
    del m[0:(len(m))]
    print(m)


#   chop(p)
#   print(type(chop(p)))

def is_sorted(m):
    if m == sorted(m):
        return True
    else:
        return False


#   print(is_sorted(p))


def is_anagram(x, y):
    m1 = sorted(list(x))
    m2 = sorted(list(y))
    if len(m1) != len(m2):
        print("No")
    else:
        if m1 == m2:
            print("Yes")
        else:
            print("No")


#   is_anagram("part", "trap")
k = [1, 2, 3, 3, 4, 5, 6, 6, 6]


def remove_duplicates(m):
    temp = []
    for x in m:
        if x not in temp:
            temp.append(x)
    print(temp)


#   remove_duplicates(k)
t = "word.txt"


def create_list_1(m):
    start_time = time.time()
    result = []
    with open(m) as f:
        lines = f.readlines()
    result.append(lines)
    print(result)
    end_time = time.time()
    tm_1 = end_time - start_time
    print(tm_1)


#  create_list_1(t)


def create_list_2(m):
    start_time = time.time()
    result = []
    with open(m) as f:
        lines = f.readlines()
    result = result + [lines]
    print(result)
    end_time = time.time()
    tm = end_time - start_time
    print(tm)


#   create_list_2(t)

#   look up bisect built-in function
