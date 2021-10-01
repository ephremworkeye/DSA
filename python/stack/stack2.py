class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def push(self, value):
        newNode = Node(value)
        if not self.top:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.height += 1
    
    def pop(self):
        if self.height == 0:
            return None
        current = self.top
        self.top = self.top.next
        self.height -= 1
        return current.value

    def print_stack(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next

stack = Stack()
stack.push(4)
stack.push(3)
stack.push(2)

stack.print_stack()
print(f'popped element is {stack.pop()}')
stack.print_stack()

       