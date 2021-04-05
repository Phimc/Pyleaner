from decimal import *
n = int(input())

getcontext().prec = n
t = 1
d = Decimal (10**(-n))
def pi(x):
    t1 = Decimal((2**0.5)/2)
    t2 = Decimal(2**0.5)
    for i in range(x):
        t2 = Decimal((t2)+Decimal (2**0.5))
        t1 = Decimal(t1*t2/2)
    return Decimal(2/t1)

while pi(t+1)-pi(t) > d:
    t = t+1
print(t+2)
print(d)
print(Decimal(pi(t+2)))