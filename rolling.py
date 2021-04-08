n = int(input())
d = int(input())
a = [[0]*d for i in range(d)]
direct = 0
x = 0
y = 0
for i in range(d*d):
    q = i%n+1
    a[x][y] = i % n+1
    if direct == 0:
        if y+1 < d and a[x][y+1] == 0:
            y += 1
        else:
            x += 1
            direct = 1
    elif direct == 1:
        if x+1 < d and a[x+1][y] == 0:
            x += 1
        else:
            y -= 1
            direct = 2
    elif direct == 2:
        if a[x][y-1] == 0:
            y -= 1
        else:
            x -= 1
            direct = 3
    else:
        if a[x-1][y] == 0:
            x -= 1
        else:
            y += 1
            direct = 0
for i in a:
    s = [str(j) for j in i]
    print(" ".join(s))