from __future__ import annotations
from node import Node


class BST:
    def __init__(self, root):
        if isinstance(root, Node):
            self.root = root
        else:
            self.root = Node(root)
            

    def insert(self, data, start=None):
        if start is None:
            start = self.root

        node = Node(data)

        if start is None:
            start = node
            return

        # left
        if node <= start:
            if start.left is None:
                start.left = node
            else:
                insert(data, start.left)

        # right
        if node > start:
            if start.right is None:
                start.right = node
            else:
                insert(data, start.right)

        


    def preOrder(self, start: Node=None):
        if start is None:
            start = self.root
            print("Pre order:", end=' ')

        print(f"{start.data},", end=' ')

        if start.left is not None:
            self.preOrder(start.left)
        
        if start.right is not None:
            self.preOrder(start.right)


    def inOrder(self, start: Node=None):
        if start is None:
            start = self.root
            print("In order:", end=' ')

        if start.left is not None:
            self.inOrder(start.left)

        print(f"{start.data},", end=' ')

        if start.right is not None:
            self.inOrder(start.right)
