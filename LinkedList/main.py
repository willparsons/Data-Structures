from linkedlist import *

def main():
    ll = LinkedList(1)
    ll.add(2)
    ll.add(3)

    ll.replaceHead(4)

    ll.insertAfter(2, 6)

    ll.remove(1)
    
    ll.printList()
    

if __name__ == "__main__":
    main()