time = 0
N,M = map(int,input().split())
fire = list(map(int,input().split()))
dis = []
minute = []
for f in fire:
    dis.append(f-1)
for i in range(1,len(dis)):
    minute.append((int(((dis[i]-dis[i-1]-1))/2)+1))
minute.append(fire[0])
minute.append(N-fire[-1]+1)
mins = 0
for mini in minute:
    if mini>mins:
        mins = mini
print(mins)