'''
line_n = int(input())
line_need = []
engine_p = []
available = 0
for i in range(line_n):
    line_need.append(int(input()))
engine_n = int(input())
for i in range(engine_n):
    engine_p.append(int(input()))
line_need.sort()
engine_p.sort()
for engine in engine_p:
    for i in range(len(line_need)):
        if line_need[i] <= engine:
            line_need.pop(i)
            available += 1
            break
print(available)
'''
