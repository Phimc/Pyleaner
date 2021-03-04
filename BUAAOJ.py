n = int(input())
tcode = []

for i in range(n):
    tcode.append(list(input()))

for i in range(n):    
    while '\t' in tcode[i]:
        tcode[i][tcode[i].index('\t')] = '    '
    
    space = 0
    for j in range(len(tcode[i])):
        if tcode[i][j] != ' ':
            break
        else:
            space += 1
    if space % 4 != 0:
        space = 4-(space % 4)
        for k in range(space):
            tcode[i].insert(0,' ')
    
    while '#' in tcode[i]:
        if tcode[i][tcode[i].index('#')+1] != ' ':
            tcode[i][tcode[i].index('#')] = '# '
            break    
 
for i in range(n):
    print(''.join(tcode[i]))

