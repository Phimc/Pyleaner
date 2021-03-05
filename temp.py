n = int(input())
d = 10**(-n)
t = 1
def pi(x):
    t1 = (2**0.5)/2
    t2 = 2**0.5
    for i in range(x):
        t2 = (t2+2)**0.5
        t1 = t1*t2/2
    return 2/t1

while abs(pi(t+1)-pi(t)) > d:
    t = t+1
print(t+2)
print(round(pi(t+2),n))