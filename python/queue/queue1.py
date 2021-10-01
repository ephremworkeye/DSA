class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        current = self.head
        if self.length == 1:
            self.head  = None
            self.tail = None
        else:
            self.head = self.head.next
            current.next = None
            self.length -= 1
        return current.value

    def print_queue(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


queue = Queue()
queue.enqueue(4)
queue.enqueue(3)
queue.enqueue(2)
queue.print_queue()
print(f"dequed element is: {queue.dequeue()}")
queue.print_queue()