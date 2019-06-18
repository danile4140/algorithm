# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/6/16
    @dec: 堆
"""


class Heap:
    def __init__(self, array: list = None, is_large=True):
        """
        :param is_large: 是否是大顶堆
        """
        self.__array = array if array else [None]
        self.__is_large_heap = is_large
        self.build_heap(self.count)

    def __repr__(self):
        return "{}".format(self.__array)

    @property
    def count(self):
        """堆存储数据的个数"""
        return len(self.__array) - 1

    def insert(self, data):
        """堆的插入"""
        self.__array.append(data)
        i = self.count
        while i > 0:
            p = int(i / 2)
            if p > 0 and (
                    self.__array[i] > self.__array[p] if self.__is_large_heap else self.__array[i] < self.__array[p]):
                self.__array[i], self.__array[p] = self.__array[p], self.__array[i]
            i = p

    def build_heap(self, n):
        for i in range(int(n / 2), 0, -1):
            self.heapify(n , i)

    def heapify(self, n, i):
        """自上而下的堆化"""
        max_pos = i
        while True:
            if i * 2 <= n and (
                    self.__array[i] < self.__array[i * 2] if self.__is_large_heap else self.__array[i] > self.__array[
                        i * 2]):
                max_pos = i * 2
            if i * 2 + 1 <= n and (
                    self.__array[max_pos] < self.__array[i * 2 + 1] if self.__is_large_heap else self.__array[max_pos] >
                                                                                                 self.__array[
                                                                                                     i * 2 + 1]):
                max_pos = i * 2 + 1
            if max_pos == i: break
            self.__array[i], self.__array[max_pos] = self.__array[max_pos], self.__array[i]
            i = max_pos

    def remove(self):
        """堆顶删除"""
        if self.count == 0:
            print(self)
            return
        if self.count == 1:
            self.__array.pop()
            print(self)
            return
        self.__array[1] = self.__array.pop()
        self.heapify(self.count, 1)
        print(self)

        # todo 堆的应用  优先级队列、求 Top K 问题和求中位数问题。

    def sort(self):
        """堆排序，从小到大"""
        k = self.count
        while k > 1:
            self.__array[1], self.__array[k] = self.__array[k], self.__array[1]
            k -= 1
            self.build_heap(k)


if __name__ == '__main__':
    h = Heap(is_large=True)
    h.insert(3)
    h.insert(1)
    h.insert(5)
    h.insert(2)
    h.insert(6)
    print(h)
    h.remove()
    h.remove()
    l = [None, 7, 5, 19, 8, 4, 1, 20, 13, 16]
    h1 = Heap(array=l)
    print(h1)
    h1.sort()
    print(h1)