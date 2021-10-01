class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLInkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_doubly_linked(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1
        return True

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        else:
            current = self.tail
            if self.head === self.tail:
                self.tail = None
                self.head = None
            else:
                self.tail = self.tail.previous
                self.tail.next = None
                current.previous = None
            self.length -= 1
            return current

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.head is None:
            return None
        else:
            current = self.head
            if self.head = self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.previous = None
                current.next = None
            self.length -= 1
            return current

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length //  2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length -1, index, -1):
                current = current.previous
        return current     

    def set_value(self, index, value):
        if index < 0 index >= self.length:
            return None
        
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
            current.value = value
        else:
            current = self.tail
            for _ in range(self.length-1, index, -1):
                current = current.previous
            current.value = value


    def insert(self, index, value):
        



        
dls = DoublyLInkedList()
dls.append(5)
dls.append(4)
dls.append(2)
dls.prepend(10)
dls.print_doubly_linked()
print(dls.length)
dls.pop()

dls.print_doubly_linked()
print(dls.length)
