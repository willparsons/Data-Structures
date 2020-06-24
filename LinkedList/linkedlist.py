from LinkedList.node import Node


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = Node(data)

    def insert_at_head(self, data):
        node = Node(data)

        if self.head is not None:
            node.next = self.head

        self.head = node

    def insert_after(self, after, data):
        current = self.head

        while current is not None:
            if current.data == after:
                new_node = Node(data)

                if current.next is not None:
                    new_node.next = current.next

                current.next = new_node
                return
            current = current.next

        raise Exception("Node not found")

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next

            current = current.next

    def delete_at_head(self):
        if self.head.next is not None:
            self.head = self.head.next
        else:
            self.head = None

    def search(self, data):
        if self.is_empty():
            return None

        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next

    def is_empty(self):
        return self.head is None

    def print_list(self):
        current = self.head
        while current is not None:
            print("{} ->".format(current.data), end=' ')
            current = current.next
