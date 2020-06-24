from queue import Queue

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    while not q.is_empty():
        print(f"Removing from queue: {q.top()}")
        q.dequeue()




