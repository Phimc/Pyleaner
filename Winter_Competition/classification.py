#初始化学校代码字典
# key：代码 
# value：学校
schoolcode = {}
while True:
    da = input().split()
    if da != ['stop']:
        schoolcode[int(da[0])] = da[1]
    else:
        break


#初始化学科评估等级字典
#key：等级 
#value ：[学校代码A，学校代码B]
clsch = {}
classes = ['A+','A','A-','B+','B','B-','C+','C','C-']
school = []
c = ''
while True:
    cla = input().split()
    if cla != ['stop']:
        if cla[0] in classes:
            c = cla[0]
            school = []
            clsch[c] = school
        else:
            school.append(int(cla[0]))
            clsch[c] = school
    else:
        break

print('OK')