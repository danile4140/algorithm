# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/6/11
    @dec: 二叉查找树
"""
from binarytree import bst, Node


def find(root, value):
    if root is None:
        print(-1)
        return
    if root.value == value:
        print(root.value)
        return
    find(root.left if root.value > value else root.right, value)


def insert(root, value):
    node = Node(value)
    if root is None:
        print(-1)
        return
    if root.value > value and root.left is None:
        root.left = node
        return
    if root.value <= value and root.right is None:
        root.right = node
        return
    insert(root.left if root.value >= value else root.right, value)


def delete(root, value):
    if root is None:
        print(-1)
        return
    if root.value == value:
        print("sign {} deleted.".format(root.value))
        return
    delete(root.left if root.value > value else root.right, value)


def height(root):
    if root is None:
        return -1
    return max(height(root.left), height(root.right)) + 1


if __name__ == '__main__':
    root = bst(height=2)
    print(root)
    # find(root, 0)
    # insert(root, 8)
    # print(root)
    # delete(root, 3)
    print(height(root))
