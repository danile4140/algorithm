# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/29
    @dec: 栈
"""
from DataStructure.SingleLinkedList import Node


class SequenceStack:
    """顺序栈"""

    def __init__(self, size):
        self.stack = []
        self.size = size
        self.count = 0

    def push(self, value):
        """入栈"""
        if self.size == self.count:
            print("stack is full")
            return False

        self.stack.append(value)
        self.count += 1
        return True

    def pop(self):
        """出栈"""
        if self.count == 0:
            print("stack is empty")
            return

        self.count -= 1
        print(self.stack.pop())


class LinkedStack:
    """链式栈"""

    def __init__(self, size):
        self.size = size
        self.count = 0
        self.head = None
        self.tail = None

    def push(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.count += 1
            return True

        if self.size == self.count:
            print("stack is full")
            return False
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.count += 1
        return True

    def pop(self):
        if self.tail is None:
            print("stack is empty")
            return
        if self.count == 1:
            print(self.head.data)
            self.head = self.tail = None
            self.count -= 1
            return
        p = self.head
        cur = p
        while p.next is not None:
            cur = p
            p = p.next
        value = p.data
        cur.next = None
        self.tail = cur
        self.count -= 1
        print(value)


if __name__ == '__main__':
    sa = SequenceStack(5)
    sa.push(3)
    sa.push('2')
    sa.push(3)
    sa.push(4)
    sa.push(1)
    sa.push(6)
    sa.push(8)
    sa.pop()
    sa.pop()
    sa.pop()
    sa.pop()
    sa.pop()
    sa.pop()
    print("^^^^^^^^^^")
    ls = LinkedStack(5)
    ls.push(3)
    ls.push('2')
    ls.push(3)
    ls.push(4)
    ls.push(1)
    ls.push(6)
    ls.push(8)
    ls.pop()
    ls.pop()
    ls.pop()
    ls.pop()
    ls.pop()
    ls.pop()
