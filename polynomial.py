# -*- coding: utf-8 -*-
# 利用链表实现多项式求和
import sys
sys.path.append('~/python/data_algorithm')
import linkedlist1

# 设置两个测试用的链表
poly1 = linkedlist1.SinCycLinkedList()
poly2 = linkedlist1.SinCycLinkedList()
poly1.add(12)
poly1.add(2)
poly1.add(3)
poly2.add(4)
poly2.add(3)
poly2.add(14)


def ZeroPolynomial(maxdegree):  # 多项式初始化,输入为多项式次数
    s = linkedlist1.SinCycLinkedList()
    for i in range(maxdegree):
        s.add(0)
    return s


#  利用链表的加法，计算多项式求和
def AddPolynomial(poly1, poly2, maxdegree=max(poly1.size(), poly2.size())):
    s = ZeroPolynomial(maxdegree)
    prev = s.head
    prev1 = poly1.head
    prev2 = poly2.head
    while prev is not None:
        cur = prev.getNext()
        cur1 = prev1.getNext()
        cur2 = prev2.getNext()
        if cur is None:
            break
        cur.setData(cur1.getData() + cur2.getData())
        prev = cur
        prev1 = cur1
        prev2 = cur2
    return s

a = AddPolynomial(poly1, poly2)
print '-----'
prev = a.head
while prev is not None:  # 打印多项式求和后的系数
    cur = prev.getNext()
    if cur is None:
        break
    print cur.getData()
    prev = cur
print '----'
print a.size(), poly1.size(), poly2.size()
