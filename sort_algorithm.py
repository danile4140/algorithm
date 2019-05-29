# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: dengchao
    @time: 2018/11/11
    @dec: 各种排序算法和查找算法
"""
import queue


def binary_search(list, item):
    """
    二分查找
    :param list: 一个有序的数组/列表
    :param item: 待查找元素
    :return: 元素在位置
    """
    low = 0
    high = len(list) - 1
    print(list)
    while low <= high:
        mid = int((low + high) / 2)
        if list[mid] == item:
            return mid
        elif list[mid] < item:
            low = mid + 1
        elif list[mid] > item:
            high = mid - 1
    return None


def select_sort(list):
    """选择排序"""
    new_list = []
    while list:
        small = min(list)
        new_list.append(list.dequeue())
    return new_list


def fast_sort(list):
    """快速排序"""
    # 基线条件
    if len(list) < 2:
        return list
    pivot = list[0]
    left = [i for i in list[1:] if i <= pivot]
    right = [i for i in list[1:] if i > pivot]
    return fast_sort(left) + [pivot] + fast_sort(right)


def greedy_algorithm():
    """贪婪算法"""
    stations = dict()
    stations["a"] = set([1, 2, 3, 4])
    stations["b"] = set([2, 5, 6])
    stations["c"] = set([2, 3, 4, 5, 6, 7])
    stations["d"] = set([5, 6, 7,9])
    final_stations = set()
    need_coverd = set()
    for k, v in stations.items():
        need_coverd |= v
    while need_coverd:
        best_station = None
        states_coverd = set()
        for k, v in stations.items():
            coverd = need_coverd & v
            if len(coverd) > len(states_coverd):
                states_coverd = coverd
                best_station = k
        final_stations.add(best_station)
        need_coverd -= states_coverd
    print(final_stations)

def sum(list):
    if list:
        return list.dequeue() + sum(list)
    else:
        return 0


if __name__ == '__main__':
    list = [5, 4, 6, 2, 5, 7, 8, 2, 3, 4, 5]
    # binary_search(sorted(list), 3)
    # print(select_sort(list))
    # print(fast_sort(list))
    a = float("inf")
    greedy_algorithm()
    exit(0)
