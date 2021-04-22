class WM:
    def __init__(self,n):
        """index:{序号：名称}
        rule: {名称：序号}
        stack：容器
        v：容器容量"""
        self.index = {0:"grape", 1:"cherry", 2:"orange", 3:"lemon", 4:"kiwifruit", 5:"tomato", 6:"peach",7: "pineapple", 8:"coconut",9: "watermelon", 10:"WATERMELON"}
        self.rule = {"grape":0, "cherry":1, "orange":2, "lemon":3, "kiwifruit":4, "tomato":5, "peach":6, "pineapple":7, "coconut":8, "watermelon":9, "WATERMELON":10}
        self.stack = []
        self.v = n
    
    def not_FULL(self):
        """容量是否没满"""
        if self.stack == []:
            return True
        elif len(self.stack) < self.v :
            return True
        else:
            return False
    def add(self,A,B):
        """合成A,B:能合成则返回合成后的水果，如果不能则将A置于容器并且返回B"""
        if self.rule[A]==self.rule[B]:
            return self.index[self.rule[A]+1]
        else:
            self.stack.append(A)
            return B
            
    def throw(self,fruit):
        """将fruit置于容器"""
        if self.not_FULL():
            if self.stack != []:
                last_fruit = self.stack.pop()
                fi = self.add(last_fruit,fruit)
                if fi != fruit:
                    self.throw(fi)
                else:
                    self.stack.append(fi)
            else:
                self.stack.append(fruit)
        else:
            last_fruit = self.stack.pop()
            fi = self.add(last_fruit,fruit)
            if fi == fruit:
                raise Exception
            else:
                self.stack.append(fi)
                self.throw(self.stack.pop())
    
    def checkwin(self):
        if 'WATERMELON' in self.stack:
            return 'WIN'
        else:
            return 'NO'
    
    def printa(self):
        print(' '.join(self.stack))

N,M = map(int,input().split())
WM_0 = WM(N)
fruits = []
flag = 1
for i in range(M):
    fruits.append(input())
if N!= 0:
    if M != 0:
        for fruit in fruits:
            try:    
                WM_0.throw(fruit)
                if WM_0.checkwin() == 'WIN':
                    print('You win!')
                    break
                elif WM_0.checkwin() == 'NO':
                    continue
            except:
                print('You lose!')
                flag = 0
                break
        if flag:
            if WM_0.checkwin() != 'WIN':
                print('You lose!')
        WM_0.printa()
    else:
        print('You lose!')
        print('')
else:
    print('You lose!')
    print('')