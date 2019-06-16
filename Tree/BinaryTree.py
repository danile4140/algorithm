# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @author: kyou
    @date: 2019/6/9
    @dec: 二叉树
"""

from binarytree import tree


def pre_order(root):
    """前序遍历"""
    if root is None:
        return
    print(root.value)
    pre_order(root.left)
    pre_order(root.right)


def in_order(root):
    """中序遍历"""
    if root is None:
        return
    in_order(root.left)
    print(root.value)
    in_order(root.right)


def post_order(root):
    """后序遍历"""
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.value)


def level_order(root):
    """层序遍历"""
    # 如果根节点为空，则返回空列表
    if root is None:
        return
    # 模拟一个队列储存节点
    q = []
    # 首先将根节点入队
    q.append(root)
    # 列表为空时，循环终止
    while len(q) != 0:
        length = len(q)
        for i in range(length):
            # 将同层节点依次出队
            r = q.pop(0)
            if r.left is not None:
                # 非空左孩子入队
                q.append(r.left)
            if r.right is not None:
                # 非空右孩子入队
                q.append(r.right)
            print(r.value)


if __name__ == '__main__':
    t = tree(height=3, is_perfect=False)
    print(t)
    # pre_order(t)
    # in_order(t)

    level_order(t)