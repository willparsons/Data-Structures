from node import *

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    
    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = Node(data)


    def insertAfter(self, after, data):
        current = self.head
        
        while current.next is not None:
            if current.data == after:
                newNode = Node(data)
                newNode.next = current.next
                current.next = newNode
                return
            current = current.next

        raise Exception("Node not found")


    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                
            current = current.next

    
    def replaceHead(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    
    def printList(self):
        current = self.head
        while current is not None:
            print("{} ->".format(current.data), end = ' ')
            current = current.next