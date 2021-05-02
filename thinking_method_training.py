n,r,b = map(int,input().split())
k = 0
Ri = list(map(int,input().split()))
Bi = list(map(int,input().split()))
q = Ri + Bi
q.sort()
def check_same(i,j):
    if bool(i in Ri)^bool(j in Ri):
        return False
    else:
        return True
def getk_diffcolor(p,q):
    if (p-q)%2 == 0:
        return 1
    else:
        return 0
def getk_samecolor(p,q):
    if (q-p) % 2:
        return 1
    else:
        return 0
for i in range(len(q)-1):
    if check_same(q[i],q[i+1]):
        k += getk_samecolor(q[i],q[i+1])
    else:
        k += getk_diffcolor(q[i],q[i+1])
print(k)