n = int(input())
place = [0 for i in range(n+1)]
def grow(i,j):
    if (j-i+1) >= 3:
        if (j-i+1) % 2:
            mid = int((j+i)/2)
        else:
            mid = int((j+i+1)/2)
        place[mid] = 1
        grow(i,mid-1)
        grow(mid+1,j)
    else:
        return 0
grow(1,n)
answer = []
for j in range(n+1):
    if place[j]:
        answer.append(j)
answer.sort()
print(' '.join(list(map(str,answer))))