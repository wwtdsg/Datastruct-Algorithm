# -*- coding: utf-8 -*-
# python的二叉树的类实现
# references: www.cnblogs.com/linxiyue/p/3570071.html


class BinaryTree():
    def __init__(self, item):
        self.key = item
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, item):
        if self.leftChild is None:
            self.leftChild = BinaryTree(item)
        else:
            temp = BinaryTree(item)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self, item):
        if self.rightChild is None:
            self.rightChild = BinaryTree(item)
        else:
            temp = BinaryTree(item)
            temp.rightChild = self.rightChild
            self.rightChild = temp


def InfixExpressionTree(exp):  # 根据中缀表达式构造表达式树
    tree = BinaryTree('')
    stack = []
    stack.append(tree)
    currentTree = tree
    for i in exp:
        if i == '(':
            currentTree.insertLeft('')
            stack.append(currentTree)
            currentTree = currentTree.leftChild
        elif i not in '+-*/()':
            currentTree.key = int(i)
            parent = stack.pop()
            currentTree = parent
        elif i in '+-*/':
            currentTree.key = i
            currentTree.insertRight('')
            stack.append(currentTree)
            currentTree = currentTree.rightChild
        elif i == ')':
            currentTree = stack.pop()
        else:
            raise ValueError
    return tree


def PostfixExpressionTree(exp):  # 根据后缀表达式构造表达式树
    stack = []
    for i in exp:
        if i not in '+-*/':
            tree = BinaryTree(int(i))
            stack.append(tree)
        else:
            rightTree = stack.pop()
            leftTree = stack.pop()
            tree = BinaryTree(i)
            tree.leftChild = leftTree
            tree.rightChild = rightTree
            stack.append(tree)
    return tree


def inorder(tree):  # 中序遍历
    if tree:
        inorder(tree.leftChild)
        print tree.key
        inorder(tree.rightChild)


def postorder(tree):  # 后序遍历
    if tree:
        postorder(tree.leftChild)
        postorder(tree.rightChild)
        print tree.key

# 测试代码
Iexp = '((1+2)+(3+(4*5)))'  # 中缀表达式
I = InfixExpressionTree(Iexp)

Pexp = '12+345+**'  # 后缀表达式
p = PostfixExpressionTree(Pexp)

postorder(I)
print '----'
inorder(I)
