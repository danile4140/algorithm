# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/6/1
    @dec: 归并排序
"""


def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = int(len(array) / 2)
    # 分治递归
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)


def merge2(left, right):
    """哨兵实现"""
    pass


def merge(left, right):
    """普通实现"""
    i, j = 0, 0
    tmp = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
    if i != len(left):
        tmp += left[i:]
    else:
        tmp += right[j:]
    print(tmp)
    return tmp


if __name__ == '__main__':
    l = [2, 1, 9, 7, 6, 5, 8, 3, 4]
    print(merge_sort(l))
