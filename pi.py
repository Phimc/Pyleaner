name = input()
age = input()
birth = list(map(int,input().split()))
print('我是%s，今年%s岁，%d年%02d月出生'%(name,age,birth[0],birth[1]))