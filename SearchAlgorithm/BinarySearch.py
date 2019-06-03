# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/6/2
    @dec: 二分查找
"""


# import numpy


def binary_search(sorted_array, low, high, value):
    """
    二分查找,递归
    :param sorted_array: 有序的数组
    :param value: 查找的值
    :return: 返回值的index
    """
    mid = int((low + high) / 2)
    if low > high:
        return -1
    if sorted_array[mid] == value:
        return mid
    elif sorted_array[mid] > value:
        high = mid - 1
        return binary_search(sorted_array, low, high, value)
    else:
        low = mid + 1
        return binary_search(sorted_array, low, high, value)


def b_search(sorted_array, value):
    """二分查找"""
    low = 0
    high = len(sorted_array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if sorted_array[mid] < value:
            low = mid + 1
        elif sorted_array[mid] > value:
            high = mid - 1
        else:
            return mid
    return -1


def sqrt(num, low, high, digital=6):
    """
    利用二分查找实现平方根
    :param num: 要求解的数字
    :param digital: 保留多少位小数
    :return:
    """
    # if num < 0:
    #     return -1
    # count = 0
    # low = 0
    # high = num
    # ans = (low + high) / 2.0
    # sign = ans
    # while ans ** 2 != num and count < digital:
    #     if ans ** 2 > num:
    #         high = ans
    #     else:
    #         low = ans
    #     ans = (low + high) / 2.0
    #     count += 1
    #     if sign == ans:
    #         break
    # print(ans)
    r = 1 / 10 ** digital

    mid = (low + high) / 2
    if num - mid * mid < 0:
        return sqrt(num, low, (mid + high) / 2, digital)
    elif num - mid * mid > r:
        return sqrt(num, (low + mid) / 2, high, digital)

    return "%.6f" % mid


def b_search_1(array, value):
    """查找第一个值等于给定值的元素位置"""
    low = 0
    high = len(array) - 1
    index = -1
    while low <= high:
        mid = int((low + high) / 2)
        if array[mid] == value:
            index = mid
            high = mid - 1
        elif array[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return index


def b_search_1_1(array, value):
    """查找第一个值等于给定值的元素位置(教程)"""
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if array[mid] > value:
            high = mid - 1
        elif array[mid] < value:
            low = mid + 1
        else:

            if array[mid - 1] < value or mid == 0:
                return mid
            else:
                high = mid - 1
    return -1


def b_search_1_2(array, value):
    """查找第一个值等于给定值的元素位置(烧脑版)"""
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if array[mid] >= value:
            high = mid - 1
        else:
            low = mid + 1
    if low < len(array) and array[low] == value:
        return low
    return -1


def b_search_2(array, value):
    """查找最后一个值等于给定值的元素位置"""
    low = 0
    high = len(array) - 1
    index = -1
    while low <= high:
        mid = int((low + high) / 2)
        if array[mid] == value:
            index = mid
            low = mid + 1
        elif array[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return index


def b_search_3(array, value):
    """查找第一个大于等于给定值的元素位置"""
    low = 0
    high = len(array) - 1
    index = -1
    while low <= high:
        mid = int((low + high) / 2)
        if array[mid] == value:
            index = mid
            high = mid - 1
        elif array[mid] > value:
            index = mid
            high = mid - 1
        else:
            low = mid + 1
    return index


def b_search_3_3(array, value):
    """查找第一个大于等于给定值的元素位置(教程)"""
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if array[mid] >= value:
            if array[mid - 1] < value or mid == 0:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1


def b_search_4(array, value):
    """查找最后一个小于等于给定值的元素位置"""
    low = 0
    high = len(array) - 1
    index = -1
    while low <= high:
        mid = int((low + high) / 2)
        if array[mid] == value:
            index = mid
            low = mid + 1
        elif array[mid] < value:
            index = mid
            low = mid + 1
        else:
            high = mid - 1
    return index


if __name__ == '__main__':
    # l = numpy.random.randint(10, size=10)
    l = [1, 3, 3, 5, 5, 5, 7, 8, 9, 10]
    # print(b_search(l, 81))
    # print(binary_search(l, 0, len(l) - 1, 8))
    # print(sqrt(2, 0, 2))
    print(b_search_1_2(l, 5))
