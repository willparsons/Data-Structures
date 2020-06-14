from __future__ import annotations

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __lt__(self, other: Node):
        return self.data < other.data

    def __le__(self, other: Node):
        return self.data <= other.data

    def __gt__(self, other: Node):
        return self.data > other.data

    