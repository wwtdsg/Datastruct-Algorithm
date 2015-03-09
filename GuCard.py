#! -*- coding:utf-8 -*-
"""
N张骨牌排成一行，按顺序编号为1，2，3，……，N-1，N。第一次
拿走所有奇数位置上的骨牌，第二次再从剩余骨牌中拿走所有奇
数位置上的骨牌，以此类推，求最后剩下的一张骨牌编号。
"""


class GuCard:
    def __init__(self, num):
        self.num = num
        self.arr = range(num + 1)
        del self.arr[0]

    def delet(self):
        while len(self.arr) > 1:
            temp = []
            for i in range(len(self.arr)):
                if i % 2 == 1:
                    temp.append(self.arr[i])
            self.arr = temp
        return self.arr


gu = GuCard(904)
gu.delet()
print gu.arr
