from node import Node
from typing import List


class Stack:
    def __init__(self):
        self.__elements: List[Node] = []

    def push(self, data):
        node = Node(data)
        self.__elements.append(node)

    def pop(self):
        return self.__elements.pop().data

    def is_empty(self):
        return len(self.__elements) == 0

    def top(self):
        return self.__elements[-1].data
