#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def depth_max(node, depth):
    if node is None:
        return -100000
    
    if depth == 0:
        return node.value
    
    left_value = depth_max(node.left, depth - 1)
    right_value = depth_max(node.right, depth - 1)
    
    return max(left_value, right_value)


if __name__ == '__main__':
    root = BinaryTreeNode(
        3,
        BinaryTreeNode(1, BinaryTreeNode(0), None),
        BinaryTreeNode(5, BinaryTreeNode(4), BinaryTreeNode(6)),
    )
    limit = 2

    result = depth_max(root, limit)
    print(f"Максимальное значение на указанной глубине: {result}")