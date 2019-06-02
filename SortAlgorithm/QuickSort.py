# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/6/2
    @dec: 快速排序
"""


def partition2(array, low, high):
    """进阶版"""
    # key的取值方式可以优化
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def partition(nums, left, right):
    """简单版"""
    key = nums[left]
    while left < right:
        # right下标位置开始，向左边遍历，查找不大于基准数的元素
        while left < right and nums[right] >= key:
            right -= 1
        if left < right:  # 找到小于准基数key的元素,然后交换nums[left],nums[right]
            nums[left], nums[right] = nums[right], nums[left]
        else:  # left〉=right 跳出循环
            break
        # left下标位置开始，向右边遍历，查找不小于基准数的元素
        while left < right and nums[left] < key:
            left += 1
        if left < right:  # 找到比基准数大的元素，然后交换nums[left],nums[right]
            nums[right], nums[left] = nums[left], nums[right]
        else:  # left〉=right 跳出循环
            break
    return left  # 此时left==right 所以返回right也是可以的


def quick_sort(array, low, high):
    if low < high:
        key_index = partition2(array, low, high)

        quick_sort(array, low, key_index)
        quick_sort(array, key_index + 1, high)


def quick_sort_find(array, low, high, k):
    """找数组中第k大的元素"""
    rst = None
    if low < high:
        key_index = partition2(array, low, high)
        if key_index + 1 < k:
            rst = quick_sort_find(array, key_index + 1, high, k)
        elif key_index + 1 > k:
            rst = quick_sort_find(array, low, key_index, k)
        elif key_index + 1 == k:
            rst = array[key_index]
    return rst


if __name__ == '__main__':
    array = [5, 6, 4, 2, 3, 1]
    print('原：', array)
    quick_sort(array, 0, len(array) - 1)
    print('现：', array)
    array = [5, 6, 4, 2, 3, 1]
    print(quick_sort_find(array, 0, len(array) - 1, 4))
