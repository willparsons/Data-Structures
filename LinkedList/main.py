from LinkedList.linkedlist import *


def main():
    ll = LinkedList(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)

    ll.insert_at_head(4)

    ll.insert_after(2, 6)

    ll.delete(1)

    ll.print_list()


if __name__ == "__main__":
    main()
