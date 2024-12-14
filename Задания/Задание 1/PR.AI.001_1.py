#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def path_limit(node, goal, limit, depth=0):
    if node is None:
        return False
    
    if node.value == goal:
        return True
    
    if depth >= limit:
        return False

    return (path_limit(node.left, goal, limit, depth + 1) or
            path_limit(node.right, goal, limit, depth + 1))


if __name__ == '__main__':
    root = BinaryTreeNode(
        1,
        BinaryTreeNode(2, None, BinaryTreeNode(4)),
        BinaryTreeNode(3, BinaryTreeNode(5), None),
    )
    goal = 4
    limit = 2

    found = path_limit(root, goal, limit)
    print(f"Найден на глубине: {found}")