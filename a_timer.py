import time

startt = time.time()
A,B = map(int,input().split())
N = int(input())
message = []
for i in range(N):
    message.append(list(map(int,input().split())))
achieve = [[[0]*(B+1)]*(A+1)]*(N+1)
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

endt = time.time()
print('%s'%(endt-startt))

n = int(input())
x=[]
for i in range(n):
    x.append(int(input()))
aver = int(sum(x)/n)
times = 0
for i in range(n-1):
    if x[i] < aver:
        x[i+1]-=(aver-x[i])
        times +=(aver-x[i])
    elif x[i] > aver:
        x[i+1]+=(x[i]-aver)
        times +=(x[i]-aver)
print(times)