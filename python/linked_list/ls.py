class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_linkedList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return f'removed value is {current}'
        else:
            current = self.head
            while current.next:
                previous = current
                current = current.next
            self.tail = previous
            self.tail.next = None
            self.length -= 1
            return f'removed value is {current}'

    def length_linkedList(self):
        return self.length
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
    
    def pop_first(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return f'{current} is removed'
        else:
            current = self.head
            self.head = self.head.next 
            self.length -= 1
            return f'{current} is removed'

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def set_value(self, index, value):
        # to change the value in given index
        if index < 0 or index > self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1

        elif index == 0:
            new_node.next = self.head 
            self.head = new_node
            self.length += 1
          

        elif index == self.length:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
         
        else:
            current = self.head
            for _ in range(index -1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if self.head == self.tail:
            current = self.pop_first()
            self.length -= 1
            return current.value
        if index == self.length:
            current = self.pop()
            self.length -= 1
            return current.value
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = current.next.next

    def reverse(self):
        current = self.head
        self.head = self.tail
        self.tail = current
        after = current.next
        previous = None
        while current:
            after = current.next
            current.next = previous
            previous = current
            current = after

ls = LinkedList(4)
ls.append(7)
ls.append(8)
ls.append(10)
# ls.print_linkedList()
# print(ls.pop())
# print(ls.pop())
# print(ls.pop())
# print(ls.pop())
# print(ls.pop())
# ls.print_linkedList()
# prepend
ls.prepend(3)
# ls.print_linkedList()
# print(ls.pop_first())
# ls.print_linkedList()
# print(ls.get(2))
ls.insert(0, 1)
ls.insert(6, 6)
ls.insert(1, 12)
ls.print_linkedList()
print ('--------------')
# ls.set_value(1, 20)
# print(ls.remove(1))
# print(f'length of linked list is : {ls.length_linkedList()}')
ls.reverse()
ls.print_linkedList()

