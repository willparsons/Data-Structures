from Queue.node import Node
from typing import List


class Queue:
    def __init__(self):
        self.__elements: List[Node] = []

    def enqueue(self, data):
        if isinstance(data, Node):
            self.__elements.append(data)
        else:
            self.__elements.append(Node(data))

    def dequeue(self):
        del self.__elements[0]

    def is_empty(self):
        return len(self.__elements) == 0

    def top(self):
        return self.__elements[0].data
