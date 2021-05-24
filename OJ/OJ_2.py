# 2.1
#获取年月日
year = int(input())
month = int(input())
day = int(input())
#对齐输出
print('My birthday is %d.%02d.%02d'%(year,month,day))


# 2.2
#设置起始时间，学习分钟数[小时，分钟]
time = list(map(int,input().split()))
minute = int(input())
hour = minute // 60
minute = minute % 60
#计算截止时间
time[1] += minute
time[0] += hour + (time[1] // 60)
time[1] = time[1] % 60
#判断并输出时间
if time[0] >= 23 and time[1] >= 30:
  print('23:30')
else:
  print('%02d:%02d'%(time[0],time[1]))


# 2.3
#导入函数库
import math
A = list(map(float,input().split()))
B = list(map(float,input().split()))
C = list(map(float,input().split()))
#计算三点距离和
L = math.sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)+math.sqrt((C[0]-B[0])**2+(C[1]-B[1])**2)+math.sqrt((A[0]-C[0])**2+(A[1]-C[1])**2)
print('%.2f'%L)

# 2.4
#输入行列式
D = []
for i in range(3):
  D.append(list(map(int,input().split())))
#展开并计算
De = D[0][0]*(D[1][1]*D[2][2]-D[2][1]*D[1][2])-D[1][0]*(D[0][1]*D[2][2]-D[2][1]*D[0][2])+D[2][0]*(D[0][1]*D[1][2]-D[1][1]*D[0][2])
print(De)

# 2.5
#初始值
n,m = list(map(int,input().split()))
#障碍次数
sub = 0
#指令
shoes = []
total_sub = 0
Lose = False
for i in range(n):
    shoes = list(map(int,input().split()))
    if shoes[1] == 0:
        m += shoes[0]
    else:
        m -= shoes[0]
        sub += 1
        total_sub += shoes[0]
    if m <= 0:
        Lose = True
if Lose:
    print('Sorry, you lose!')
else:
    floor = int(m/total_sub*sub)
    print(m,floor,sep=' ')