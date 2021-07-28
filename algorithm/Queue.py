class Queue:
    '''定义 Queue类 '''
    def __init__(self):
        self.items = [] #初始化空队列，队列用列表表示
    def isEmpty(self): #判断队列是否为空
        return self.items == []
    def enqueue(self, item): #入队操作
        self.items.insert(0, item) #在列表 0号位置（队尾）插入元素
    def dequeue(self): #出队操作
        return self.items.pop() #将列表尾部位置（队头）弹 出
    def size(self): #返回队列的大小
        return len(self.items)
    def get_items(self): #返回队列内元素的列表
        return self.items
