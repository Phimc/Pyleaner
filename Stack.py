class Stack():
    ''' 定义 stack 类 '''
    def __init__(self):
        self.items = [] #初始化空栈，栈使用列表表示
    def push(self, items):
        self.items.append(items) #将 items压栈
    def pop(self): #弹栈操作
        if not self.isEmpty(): #若栈非空，则返回栈顶元素
            return self.items.pop()
        else: #否则，提示 'Stack is empty!'
            raise Exception('Stack is empty!')
    def isEmpty(self): #判断栈是否为空
        return self.items == []
    def peek(self): #返回栈顶元素
        return self.items[-1]
    def size(self): #返回栈的大小
        return len(self.items)
    def get_items(self): #返回队列内元素的列表
        return self.items
