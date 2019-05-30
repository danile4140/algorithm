# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/29
    @dec: 队列
"""
from DataStructure.SingleLinkedList import Node


class SequenceQueue:
    """顺序队列"""

    def __init__(self, size):
        self.queue = []
        self.size = size
        self.count = 0
        self.pos = 0

    def __repr__(self):
        return str(self.queue)

    def enqueue(self, value):
        """入队列"""
        if self.size == self.pos + self.count:
            if self.pos == 0:
                print("queue is full")
                return False
            else:
                self.queue = self.queue[self.pos:]
                self.pos = 0

        self.queue.append(value)
        self.count += 1
        return True

    def dequeue(self):
        """出队列"""
        if self.count == 0:
            print("queue is empty")
            return

        self.count -= 1
        self.pos += 1
        # print("self.pos={}".format(self.pos))
        print(self.queue[self.pos - 1])
        if self.pos == self.size:
            self.queue = []


class LinkedQueue:
    """链式队列"""

    def __init__(self, size):
        self.size = size
        self.count = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        p = self.head
        return "({} -> {})".format(p.data, p.next)

    def enqueue(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.count += 1
            return True

        if self.size == self.count:
            print("queue is full")
            return False
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.count += 1
        return True

    def dequeue(self):
        if self.count == 0:
            print("queue is empty")
            return
        if self.count == 1:
            print(self.head.data)
            self.head = self.tail = None
            self.count -= 1
            return
        cur = self.head
        self.head = self.head.next
        self.count -= 1
        print(cur.data)


class CircleQueue:
    """循环队列"""
    pass


if __name__ == '__main__':
    sa = SequenceQueue(5)
    sa.enqueue(3)
    sa.enqueue('2')
    sa.enqueue(3)
    sa.enqueue(4)
    sa.enqueue(1)
    sa.dequeue()
    sa.dequeue()
    sa.enqueue(9)
    sa.enqueue(10)
    sa.enqueue(6)
    sa.enqueue(8)
    sa.dequeue()
    sa.dequeue()
    sa.dequeue()
    sa.dequeue()
    sa.dequeue()
    sa.dequeue()
    print("^^^^^^^^^^")
    ls = LinkedQueue(5)
    ls.enqueue(3)
    ls.enqueue('2')
    ls.enqueue(3)
    ls.dequeue()
    ls.dequeue()
    ls.enqueue(4)
    ls.enqueue(1)
    ls.enqueue(6)
    ls.enqueue(8)
    ls.dequeue()
    ls.dequeue()
    ls.dequeue()
    ls.dequeue()
    ls.dequeue()
    ls.dequeue()
