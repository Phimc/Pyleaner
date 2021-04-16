# 这是用Python模拟指针的尝试
#内存地址
addresses = [i for i in range(101)]
class memo:
    """模拟内存"""
    def __init__(self,address,data):
        self.address = address
        self.data = data

    def _p(self):
        """读址"""
        return self.address

    def p(self):
        """取值"""
        return self.data
class point:
    """指针"""
    def __init__(self,obj):
        self.obj = obj

    def _p(self):
        """读址"""
        return self.obj._p()
    def p(self):
        """取值"""
        return self.obj.p()


class link:
    def __init__(self,n):
        self.value = n
        self.next = None

for i in range(3):
    x = link(i)
