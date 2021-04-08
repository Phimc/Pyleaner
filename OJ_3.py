N,M = map(int,input().split())
fire = list(map(int,input().split()))
# 排序
fire.sort()
# 用来记录火燃过相邻点之间的时间
minute = []
def time(p,q):
    if (p-q)%2 == 0:
        return (p-q)/2
    else:
        return (p-q-1)/2

for i in range(1,len(fire)):
    minute.append(time(fire[i],fire[i-1]))
# 火势到达两端楼房的时间
minute.append(fire[0]-1)
minute.append(N-fire[-1])
mins = 0
for mini in minute:
    if mini>mins:
        mins = mini
print(int(mins+1))