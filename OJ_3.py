N,M = map(int,input().split())
fire = list(map(int,input().split()))
dis = []
minute = []
for f in fire:
    dis.append(f-1)
def time(p,q):
    if (p-q)%2 == 0:
        return (p-q)/2
    else:
        return (p-q-1)/2

for i in range(1,len(dis)):
    minute.append(time(fire[i],fire[i-1]))
minute.append(fire[0]-1)
minute.append(N-fire[-1])
mins = 0
for mini in minute:
    if mini>mins:
        mins = mini
print(mins+1)