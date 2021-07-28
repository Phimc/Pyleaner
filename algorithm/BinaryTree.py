#定义 BinaryTree类
class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None
    #定义插入左子树的操作 insert_left
    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
    #定义插入右子树的操作 insert_ right
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    #定义获取右子树的操作 get_ right _child
    def get_right_child(self):
        return self.right_child
    #定义获取左子树的操作 get_ left _child
    def get_left_child(self):
        return self.left_child
    #定义设置根节点的操作 set_root_val
    def set_root_val(self, obj):
        self.key = obj
    #定义获取根节点的操作 get_root_val
    def get_root_val(self):
        return self.key
    #定义节点的显示格式
    def __str__(self):
        return str(self.left_child)+'<--'+str(self.key)+'-->'+str(self.right_child)
    #定义先根遍历
    def preorder(self,root):
        if root==None:
            return
        print (root.key)
        self.preorder(root.left_child)
        self.preorder(root.right_child)

    #定义中根遍历历
    def midorder(self,root):
        if root==None:
            return
        self.midorder(root.left_child)
        print (root.key)
        self.midorder(root.right_child)
    #定义后根遍历
    def postorder(self,root):
        if root==None:
            return
        self.postorder(root.left_child)
        self.postorder(root.right_child)
        print (root.key)