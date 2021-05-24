r = int(input())
eu = [[0,0]]
for i in range(r):
    eu.append(list(map(int,input().split())))
n = int(input())
atk = [[0 for i in range(n+1)]]
for j in range(r):
    atk.append([-1 for i in range(n+1)])
for i in range(r+1):
    atk[i][0] = 0
for j in range(n):
    atk[0][j] = 0
'''对前i件物品,剩余j金币的atk'''
def a(i,j):
    if atk[i][j] != -1:
        if  i*j == 0:
            return 0
        else:
            return atk[i][j]
    elif eu[i][0]<=j:
        atk[i][j] = max(a(i-1,j),a(i-1,j-eu[i][0])+eu[i][1])
    else:
        atk[i][j] = a(i-1,j)
    return atk[i][j]
print(a(r,n))
'r:A,B;n:N'