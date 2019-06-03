# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/31
    @dec: 冒泡排序
"""


def bubble_sort(l: list) -> list:
    if len(l) == 1:
        return l
    n = len(l)
    while n > 0:
        # 列表有序的标记，true表示有数据交换
        flag = False

        for i in range(n - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                flag = True
            print(l)
        n -= 1
        if not flag:
            break
    return l

if __name__ == '__main__':
    l = [5, 4, 3, 6, 3, 7, 5, 6]
    print(l)
    print(bubble_sort(l))
