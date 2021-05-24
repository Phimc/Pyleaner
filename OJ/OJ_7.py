n,k = map(int,input().split())
h = list(map(int,input().split()))
for i in range(n-1,0,-1):
    if k > 0:
        if k >= h[i]:
            k -= h[i]
            h[0] += h[i]
            h[i] = 0
        else:
            h[0]+=k
            h[i]-=k
            break
    else:
        break
h = list(map(str,h))
print(' '.join(h))