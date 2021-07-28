# 商品目录类
class itemdict:
    def __init__(self):
        self.items = {}
        pass
    
    def add(self,name,code,price):
        val = {'name':name,'price':price,'q':0}
        self.items[code] = val
    def name(self,code):
        return self.items[code]['name']
    def price(self,code):
        return self.items[code]['price']
    def um(self,code):
        return self.items[code]['q'] * self.items[code]['price']
    def buy(self,code):
        self.items[code]['q'] +=1
    def num(self,code):
        return self.items[code]['q']

# 初始化商品目录        
a = itemdict()
a.add('chips',932071,3.50)
a.add('chocolate',114049,8.00) 
a.add('cookie',313903,6.50)
a.add('cupcake',955962,4.90)
a.add('milk',243813,3.20)
a.add('soap',304985,2.90)
a.add('teapot',914500,29.80)
a.add('toothbrush',961995,4.80) 
a.add('toothpaste',933328,9.30)

head = ['NAME','QUANTITY','PRICE','SUM']
while True:
    x = int(input())
    if x != 0:
        a.buy(x)
    else:
        break
#买东西
nlen = 4
qlen = 8
plen = 5
shoplist = []
for p in a.items.keys():
    if a.um(p) != 0:
        if nlen < len(a.name(p)):
            nlen = len(a.name(p))
        if qlen < len(str(a.num(p))):
            qlen = len(str(a.num(p)))
        if plen < len(str(a.price(p))):
            plen = len(str(a.price(p)))
        shoplist.append(p)
print(head[0],end=' ')
for i in range (nlen-4):
    print(' ',end='')
print(head[1],end=' ')
for i in range (qlen-8):
    print(' ',end='')
print(head[2],end=' ')
for i in range(plen-5):    
    print(' ',end='')
print(head[3])

total = 0.0
for t in shoplist:
    print(a.name(t),end= ' ')
    for i in range (nlen-len(a.name(t))):
        print(' ',end='')
    print(a.num(t),end=' ')
    for i in range (qlen-len(str(a.num(t)))):
        print(' ',end='')
    print(a.price(t),end = ' ')
    for i in range(plen-len(str(a.price(t)))):   
        print(' ',end='')
    print('%.2f'%a.um(t))
    total += a.um(t) 

print('total:%.2f\n'%total)
