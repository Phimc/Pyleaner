# 字典{"命题名":"命题值(1/-1)"}
values = {'v':'or','-':'not'}
n = int(input())
# 输入命题值与名
for i in range(n):
    varity = input().split()
    if varity[1]=='1':
        values[varity[0]] = 'True'
    else:
        values[varity[0]] = 'False'  
question = list(input())
# 字典的所有键
key = values.keys()
# 将命题名替换为值
for i in range(len(question)):
    if question[i] in key:
        question[i] = values[question[i]]
if eval(' '.join(question)):
    print(1)
else:
    print(-1)