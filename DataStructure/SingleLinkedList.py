# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/5/25
    @dec: python实现的单链表
"""


class Node:
    """链表节点"""

    def __init__(self, data=None, p=None):
        self.__data = data
        self.__next = p

    def __repr__(self):
        return "({} -> {})".format(self.__data, self.__next)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @next.deleter
    def next(self):
        self.__next = None


class SingleLinkedList:
    """单链表实现"""

    def __init__(self):
        self.head = None

    def __getitem__(self, key: int):
        if self.is_empty():
            print('linklist is empty.')
            return
        elif key < 0 or key > len(self):
            print('the given key is error')
            return
        else:
            return self._get_item(key)

    def __setitem__(self, key, value):
        if self.is_empty():
            print('linklist is empty.')
            return
        elif key < 0 or key > len(self):
            print('the given key is error')
            return
        else:
            self.delete(key)
            return self.insert(key, value)

    def __len__(self) -> int:
        p = self.head
        i = 0
        while p is not None:
            i += 1
            p = p.next
        return i

    def __repr__(self) -> str:
        p = self.head
        return "({} -> {})".format(p.data, p.next)

    def is_empty(self) -> bool:
        return len(self) == 0

    def clear(self):
        """清除单链表"""
        self.head = None

    def append(self, value):
        """添加节点"""
        node = Node(value)
        if self.is_empty():
            self.head = node
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = node

    def _get_item(self, index: int):
        if self.is_empty():
            print('Linklist is empty.')
            return
        j = 0
        p = self.head
        while p.next is not None and j < index:
            p = p.next
            j += 1
        if j == index:
            return p.data
        else:
            print('target is not exist!')

    def insert(self, index, value):
        if self.is_empty() or index < 0 or index > len(self):
            print('Linklist is empty. insert')
            return
        if index == 0:
            q = Node(value, self.head)
            self.head = q
        p = self.head
        post = self.head
        j = 0
        while p.next is not None and j < index:
            post = p
            p = p.next
            j += 1
        if index == j:
            q = Node(value, p)
            post.next = q
            q.next = p

    def delete(self, index):
        if self.is_empty() or index < 0 or index > len(self):
            print('Linklist is empty.delete')
            return

        if index == 0:
            self.head = self.head.next
            return

        cur_node = self.head
        prev_node = None
        j = 0
        while cur_node.next is not None and j < index:
            prev_node = cur_node
            cur_node = cur_node.next
            j += 1

        if index == j:
            prev_node.next = cur_node.next

    def index(self, value):

        if self.is_empty():
            print('Linklist is empty. index')
            return

        p = self.head
        i = 0
        while p.next is not None:
            if p.data == value:
                return i
            else:
                p = p.next
                i += 1
        return -1

    def __reversed__(self):
        """链表的反转"""
        if self.is_empty() or self.head.next is None:
            """单节点或者空不需要反转"""
            return self.head
        p = self.head.next
        new_p = self.head
        new_p.next = None
        while p is not None:
            # 临时存放下一个节点
            tmp = p.next
            # 当前节点反转指向前一个节点
            p.next = new_p
            # 前一个节点变为当前节点
            new_p = p
            # 设置循环的节点为临时存放的下一个节点
            p = tmp
        # 此时已经都反转了，设置重新设置一下头节点
        self.head = new_p
        return self

    def to_circle(self):
        p = self.head
        while p.next:
            p = p.next
        p.next = self.head

    def reverse(self):
        """尾部反转法"""
        if self.is_empty() or self.head.next is None:
            """单节点或者空不需要反转"""
            return self.head
        p = self.head.next
        while p.next is not None:
            q = p.next
            # 2 -> 4
            p.next = q.next
            # 3 -> 2
            q.next = self.head.next
            # 1 -> 3
            self.head.next = q
        p.next = self.head
        self.head = p.next.next
        p.next.next = None
        return self

    def is_circle(self):
        """检查是否是循环链表,快慢指针法"""
        fastp = self.head
        slowp = self.head

        while fastp is not None and fastp.next is not None:
            fastp = fastp.next.next
            slowp = slowp.next
            if fastp is slowp:
                return True
        return False

    def r_delete(self, r_index):
        """删除倒数第几个节点"""
        if r_index == 0:
            return self
        fastp = self.head
        # 待删除节点
        slowp = self.head
        # 待删除节点的前驱节点
        slowq = None
        for _ in range(r_index):
            fastp = fastp.next
        while fastp is not None:
            slowq = slowp
            fastp = fastp.next
            slowp = slowp.next
        if slowp is self.head:
            self.head = self.head.next
        else:
            slowq.next = slowp.next
        return self

    def get_mid(self):
        """求链表的中间节点，快慢指针法"""
        fastp = self.head
        slowp = self.head
        if self.is_empty():
            return None

        while fastp.next.next is not None:
            fastp = fastp.next.next
            self.next = slowp.next
            slowp = self.next
        return slowp


def merge(node1: Node, node2: Node):
    """合并两个有序链表,从小到大"""
    if node1 is None:
        return node2
    if node2 is None:
        return node1

    # 当前节点
    current = Node()
    head = current
    while node1 is not None and node2 is not None:
        if node1.data <= node2.data:
            current.next = node1
            node1 = node1.next
            current = current.next
        else:
            current.next = node2
            node2 = node2.next
            current = current.next
    if node1 is None:
        current.next = node2
    if node2 is None:
        current.next = node1
    return head.next


def merge_by_recursion(node1, node2):
    if node1 is None:
        return node2
    if node2 is None:
        return node1
    _head = Node()
    if node1.data <= node2.data:
        _head = node1
        _head.next = merge_by_recursion(node1.next, node2)
    else:
        _head = node2
        _head.next = merge_by_recursion(node1, node2.next)
    return _head


if __name__ == '__main__':
    sl = SingleLinkedList()
    sl.append(1)
    sl.append(3)
    sl.append(5)
    sl.append(7)
    sl.append(9)
    sl1 = SingleLinkedList()
    sl1.append(2)
    sl1.append(4)
    sl1.append(6)
    # print(sl)
    # print(sl1)
    # print(merge(sl.head, sl1.head))
    print(merge_by_recursion(sl.head, sl1.head))
    # sl.to_circle()
    # print(sl.is_empty())
    # sl.delete(34)
    # print(sl.index("2"))
    # sl.insert(44, "test")
    #
    # print(sl[1])
    #
    # print(reversed(sl))
    # print("^^^^" * 10)
    # print(sl.reverse())
    print(sl.is_circle())

    print(sl.r_delete(5))
