# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/31
    @dec: 插入排序
"""


def insertion_sort(array):
    if len(l) <= 1:
        return l
    n = len(array) - 1
    index = 0
    while index < n:
        _min =None
        for i in range(index, n):
            if array[i] < array[i+1]:
                temp = array[i]  # 当前需要排序的元素
                index = i  # 用来记录排序元素需要插入的位置
                while index > 0 and array[index - 1] > temp:
                    array[index] = array[index - 1]  # 把已经排序好的元素后移一位，留下需要插入的位置
                    index -= 1
                array[index] = temp  # 把需要排序的元素，插入到指定位置
            print(array)
        return array


if __name__ == '__main__':
    l = [4, 5, 6, 1, 3, 2]
    print(insertion_sort(l))
