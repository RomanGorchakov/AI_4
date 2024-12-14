#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def path_limit(node, goal, depth):
    if node is None or depth < 0:
        return None
    
    if node.value == goal:
        return node
    
    left_result = path_limit(node.left, goal, depth - 1)
    if left_result is not None:
        return left_result
    
    right_result = path_limit(node.right, goal, depth - 1)
    return right_result


if __name__ == '__main__':
    root = BinaryTreeNode(
        1,
        BinaryTreeNode(2, None, BinaryTreeNode(4)),
        BinaryTreeNode(3, BinaryTreeNode(5), None),
    )
    
    goal = 4
    limit = 2
    
    result = path_limit(root, goal, limit)
    
    if result is not None:
        print(f"Цель найдена: {result}")
    else:
        print("Цель не найдена в заданной глубине.")