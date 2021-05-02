# 40
def left_grow(i,space):
    q = []
    for j in range(i-1,-1,-1):
        if space[j]!=0:
            break
        else:
            q.append(j)
    if len(q) >= 3:
        if len(q)%2:
            space[int((q[0]+q[-1])/2)] =1
            right_grow(int((q[0]+q[-1])/2),space)
            left_grow(int((q[0]+q[-1])/2),space)
        else:
            space[int(q[0]-len(q)/2+1)] = 1
            right_grow(int(q[0]-len(q)+1),space)
            left_grow(int(q[0]-len(q)/2+1),space)

def right_grow(i,space):
    q = []
    for j in range(i+1,n):
        if space[j]:
            break
        else:
            q.append(j)
    if len(q) >= 3:
        if len(q)%2:
            space[int((q[0]+q[-1])/2)]=1
            right_grow(int((q[0]+q[-1])/2),space)
            left_grow(int((q[0]+q[-1])/2),space)
        else:
            space[int(q[0]+len(q)/2)] = 1
            right_grow(int(q[0]+len(q)/2),space)
            left_grow(int(q[0]+len(q)/2),space)
n = int(input())
if n >=3:
    space = [0 for i in range(n)]
    if n%2:
        space[int((n-1)/2)] = 1
        left_grow(int((n-1)/2),space)
        right_grow(int((n-1)/2),space)
    else:
        space[int(n/2)]=1
        left_grow(int(n/2),space)
        right_grow(int(n/2),space)
    gro=[]
    for i in range(n):
        if space[i]:
            gro.append(i+1)
    gro.sort()
    gro = list(map(str,gro))
    print(' '.join(gro))
else:
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        print(0)