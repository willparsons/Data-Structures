from __future__ import annotations
from node import Node


class BST:
    def __init__(self, root: any):
        if isinstance(root, Node):
            self.root = root
        else:
            self.root = Node(root)

    def insert(self, data, start=None):
        node = Node(data)

        if start is None:
            self.root = node
            return

        # left
        if node <= start:
            if start.left is None:
                start.left = node
            else:
                self.insert(data, start.left)

        # right
        if node > start:
            if start.right is None:
                start.right = node
            else:
                self.insert(data, start.right)

    def pre_order(self, start: Node = None):
        if start is None:
            start = self.root
            print("Pre order:", end=' ')

        print(f"{start.data},", end=' ')

        if start.left is not None:
            self.pre_order(start.left)

        if start.right is not None:
            self.pre_order(start.right)

    def in_order(self, start: Node = None):
        if start is None:
            start = self.root
            print("In order:", end=' ')

        if start.left is not None:
            self.in_order(start.left)

        print(f"{start.data},", end=' ')

        if start.right is not None:
            self.in_order(start.right)
