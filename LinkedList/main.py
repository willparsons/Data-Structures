from LinkedList.linkedlist import *


def main():
    ll = LinkedList(1)
    ll.add(2)
    ll.add(3)

    ll.replace_head(4)

    ll.insert_after(2, 6)

    ll.remove(1)

    ll.print_list()


if __name__ == "__main__":
    main()
