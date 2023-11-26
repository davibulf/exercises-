print("ex_1.")

pi = 3.14       # pi
r = 5           # radius

v = (4/3)*pi*r     # volume
print(v)

print("ex_2.")

p1 = 24.95    # initial price
p2 = p1-p1*0.4    # discounted price
s1 = 3      # shipping cost for the first copy
s2 = 0.75      # shipping cost fo each additional copy
o = 60     # books ordered

w = (p2*o)+(s1+(o-1)*s2)    # wholesale
print(w)

print("ex_3.")

T1 = (6*60*60)+(52*60)    # starting time in seconds (form 00:00)
t1 = (8*60+15)      # easy pace duration
T2 = (7*60+12)     # fast pace duration


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


# Driver program
n = (T1+t1+T2)
print(convert(n))
