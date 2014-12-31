# -*- coding: utf-8 -*-
# 链表的python实现 单循环链表


class Node:
    def __init__(self, initdata):
        self.__data = initdata
        self.__next = None

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setData(self, newdata):
        self.__data = newdata

    def setNext(self, newnext):
        self.__next = newnext


class SinCycLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.head.setNext(None)

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)

    def remove(self, item):
        prev = self.head
        while prev.getNext() is not None:
            cur = prev.getNext()
            if cur.getData() == item:
                prev.setNext(cur.getNext())
            if prev.getNext() is not None:
                prev = prev.getNext()

    def search(self, item):
        cur = self.head.getNext()
        while cur is not None:
            if cur.getData() == item:
                return True
            cur = cur.getNext()
        return False
    
    def empty(self):
        return self.head.getNext() is None

    def size(self):
        count = 0
        cur = self.head.getNext()
        while cur is not None:
            count += 1
            cur = cur.getNext()
        return count
