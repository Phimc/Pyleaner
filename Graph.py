#定义一个图中点的类
class Point:
    def __init__(self,num):
        # 初始化一个点，需要传入点的号码作为参数
        self.num = num
        self.adjacent = []
    def __eq__(self,obj):
        # 重载 __eq__函数
        # 判断两个点是否相等，依据是两个点的号码是否相等
        return self.num==obj.num
    def __str__(self):
        # 重载 __str__函数
        # 可以把一个 Point对象转换为一个字符串，方便输出
        return "结点 "+str(self.num)
#定义一个集成了图操作的类
class Graph:
    def __init__(self):
        # 以列表的形式存储图
        self.points = [] #points为图中的点
    def get_vertex(self,i):
        # 获取列表中序号为 i的那个点
        try:
            return self.points[i]
        except:
            # 如果序号 i超出了范围，那么输出错误提示信息
            print("序号 "+str(i)+"超出了范围 ")
            return None
    def add_edge(self,v,u):
        # 添加一条连接 v u的边，在 v的结点列表中加上 u，在在 u的结点列表中加上 v
        v.adjacent.append(u)
        u.adjacent.append(v)
    def next_adj(self,v,w):
        # 获取 v的邻接结点中， w的下一个邻接结点
        index_w = v.adjacent.index(w)
        try:
            return v.adjacent[index_w+1]
        except:
            # 如果没有下一个结点了，输出错误提示信息
            print(str(v)+"没有下一个邻接结点了 ")
            return None
    def add_node(self,u):
        # 给图增加一个结点
        self.points.append(u)
    def del_node(self,v):
        # 删除图中的一个点
        # 首先删 除和这个点连接的所有边
        for point in v.adjacent:
            point.adjacent.remove(v)
        # 然后把点从图的点列表中删除
        self.points.remove(v)
    def del_edge(self,v,w):
        # 从图中删除一条边
        try:
            v.adjacent.remove(w)
            w.adjacent.remove(v)
        except:
            # 如果边 v w不存在，输出错误提示信息
            print("删除边出错， ，"+str(v)+"和 "+str(w)+"不邻接 ")