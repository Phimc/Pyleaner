A,B = map(int,input().split())
N = int(input())
message = []
for i in range(N):
    message.append(list(map(int,input().split())))
achieve = [[[0 for i in range(B+1)]for j in range(A+1)]for k in range(N+1)]
def achi(i,x,y):
    if i*x*y == 0:
        return 0
    elif achieve[i][x][y] != 0:
        return achieve[i][x][y]
    elif message[i-1][0]<=x and message[i-1][1]<=y:
        achieve[i][x][y] = max(achi(i-1,x,y),achi(i-1,x-message[i-1][0],y-message[i-1][1])+message[i-1][2])
    else:
        achieve[i][x][y] = achi(i-1,x,y)
    return achieve[i][x][y]
print(achi(N,A,B))