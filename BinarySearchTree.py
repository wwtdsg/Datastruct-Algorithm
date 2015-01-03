# -*- coding: utf-8 -*-
# 二叉查找树的python实现


class BinarySearchTree():
    def __init__(self, key):
        self.key = key
        if self.key is not None:
            self.leftChild = BinarySearchTree(None)
            self.rightChild = BinarySearchTree(None)

    def find(self, x):
        if self.key == x:
            return self
        elif x < self.key and self.leftChild:
            return self.leftChild.find(x)
        elif x > self.key and self.rightChild:
            return self.rightChild.find(x)
        else:
            return None

    def insert(self, x):
        if x < self.key:
            if self.leftChild:
                self.leftChild.insert(x)
            else:
                self.leftChild = BinarySearchTree(x)
        if x > self.key:
            if self.rightChild:
                self.rightChild.insert(x)
            else:
                self.rightChild = BinarySearchTree(x)

    def findMin(self):
        if self.leftChild:
            return self.leftChild.findMin()
        else:
            return self

    def findMax(self):
        if self.rightChild:
            return self.rightChild.findMax()
        else:
            return self

    def delete(self, x):
        if self.find(x):
            if x < self.key:
                self.leftChild = self.leftChild.delete(x)
                return self
            elif x > self.key:
                self.rightChild = self.rightChild.delete(x)
                return self
            elif x == self.key:
                if self.rightChild and self.rightChild:
                    self.key = self.rightChild.findMin().key
                    self.rightChild = self.rightChild.delete(self.key)
                    return self
                elif self.leftChild:
                    return self.leftChild
                elif self.rightChild:
                    return self.rightChild
