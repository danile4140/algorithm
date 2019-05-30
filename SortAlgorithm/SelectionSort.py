# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/31
    @dec: 选择排序
"""


def selection_sort(array):
    # 这里之所以要-1，是因为首位不需要排序
    for i in range(len(array)-1):
        index = i
        for j in range(i + 1, len(array)):
            if array[index] > array[j]:
                index = j
        array[i], array[index] = array[index], array[i]
    return array


if __name__ == '__main__':
    l = [4, 5, 6, 1, 3, 2]
    print(selection_sort(l))
