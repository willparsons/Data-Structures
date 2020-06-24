from Stack.stack import Stack

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(f"Top: {s.top()}")

    while not s.is_empty():
        print(s.pop())

    print(f"Is Empty: {s.is_empty()}")
