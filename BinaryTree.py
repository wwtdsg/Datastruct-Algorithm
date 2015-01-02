# -*- coding: utf-8 -*-
# python的二叉树的类实现


class BinaryTree():
    def __init__(self, item):
        self.key = item
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, item):
        if self.leftChild is None:
            self.leftChild = item
        else:
            temp = BinaryTree()
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self, item):
        if self.rightChild is None:
            self.rightChild = item
        else:
            temp = BinaryTree()
            temp.rightChild = self.rightChild
            self.rightChild = temp
