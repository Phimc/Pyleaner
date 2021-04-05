import itertools
#消耗资金表
cost = [[6,7,11,2],[4,5,9,8],[3,1,10,4],[5,9,8,2]]
#分配任务
task = itertools.permutations([1,2,3,4],4)
min = 100000

#计算花费的最小值，记录分配方式
for taski in task:
    A1 = taski[0]
    A2 = taski[1]
    A3 = taski[2]
    A4 = taski[3]
    total = cost[0][A1-1]+cost[1][A2-1]+cost[2][A3-1]+cost[3][A4-1]
    #print(taski,end='\t')
    #print('total:%d'%total)
    if min > total:
        min = total
        solution = taski
#输出结果
print(min)
print(solution)
