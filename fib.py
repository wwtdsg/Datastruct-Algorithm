#! -*- coding:utf-8 -*-
# 裴波娜契数列优化算法
# 建立一个数组，使用一个for循环读取，比递归调用效率明显快很多


def fib(n):
    if n == 1:
        return 1
    else:
        temp = [1]
        temp.append(1)
        for i in range(n):
            temp.append(temp[i] + temp[i + 1])
        return temp[n]
print fib(10000)
