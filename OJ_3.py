time = 0
N,M = map(int,input().split())
fire = list(map(int,input().split()))
dis = [0,N-1]
minute = []
for f in fire:
    dis.insert(1,f-1)
for i in range(1,len(dis)):
    minute.append((int(((dis[i]-dis[i-1]))/2)+1))
mins = 0
for mini in minute:
    if mini>mins:
        mins = mini
print(mins)