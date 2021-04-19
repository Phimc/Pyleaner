n = int(input())
p = list(map(int,input().split()))
yougo_1 = p[0]
supfa_1 = p[1]
while n-1:
    yougo = yougo_1*0.2+supfa_1*0.6
    supfa = yougo_1*0.8+supfa_1*0.4
    yougo_1 = yougo
    supfa_1 = supfa
    n-=1
print(int(yougo_1),int(supfa_1))