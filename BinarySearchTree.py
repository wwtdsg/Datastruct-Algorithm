# -*- coding: utf-8 -*-
# 二叉查找树的python实现
""" 功能：
        1. 对于给定key进行初始化，若key是叶子，则应当具有左右为None的子树
        2. find函数，判定指定值是否位于树中
        3. insert函数，将给定值x插入到树中
        4. findMin函数，无参数，找到树中最小值
        5. findMax函数，无参数，找到树中最大值
        6. delete函数，删除给定参数所在的key
            如果key的左子树和右子树不为空，则需要将左右子树升级一层。
"""


class BinarySearchTree():
    def __init__(self, key):
        self.key = key
        if self.key is not None:
            self.leftChild = BinarySearchTree(None)
            self.rightChild = BinarySearchTree(None)

    def find(self, x):
        if self.key == x:
            return self.key
        elif x < self.key and self.leftChild.key:
            return self.leftChild.find(x)
        elif x > self.key and self.rightChild.key:
            return self.rightChild.find(x)
        else:
            return None

    def insert(self, x):
        if x < self.key:
            if self.leftChild.key:
                self.leftChild.insert(x)
            else:
                self.leftChild = BinarySearchTree(x)
        if x > self.key:
            if self.rightChild.key:
                self.rightChild.insert(x)
            else:
                self.rightChild = BinarySearchTree(x)

    def findMin(self):
        if self.leftChild.key:
            return self.leftChild.findMin()
        else:
            return self.key

    def findMax(self):
        if self.rightChild.key:
            return self.rightChild.findMax()
        else:
            return self.key

    def delete(self, x):
        if self.find(x):
            if x < self.key:
                self.leftChild = self.leftChild.delete(x)
                return self
            elif x > self.key:
                self.rightChild = self.rightChild.delete(x)
                return self
            elif x == self.key:
                if self.rightChild.key and self.leftChild.key:
                    self.key = self.rightChild.findMin()
                    self.rightChild = self.rightChild.delete(self.key)
                    return self
                elif self.leftChild.key:
                    return self.leftChild
                elif self.rightChild.key:
                    return self.rightChild
                else:
                    self.key = None
                    return self
        else:
            print "Found nothing to delete"
                

def main():
    """
    创建实例验证二叉树是否成功建立.
    """
    binary = BinarySearchTree(5)
    print "找一个不存在的数："
    print binary.find(9)
    a = [3, 2, 5, 6, 1, 8, 9]
    for i in a:
        binary.insert(i)
    print "将3删除前查找3是否存在:"
    print binary.find(3)
    binary.delete(3)
    print "将3删除后查找3是否存在"
    print binary.find(3)
    print "找一个存在的数:\n%s" % binary.find(6)
    print "查找最大值和最小值:\nmax:%s\n" % binary.findMax() + "min:%s" % binary.findMin()
    print "删除一个并不存在的数: "
    binary.delete(11)

if __name__ == "__main__":
    main()
