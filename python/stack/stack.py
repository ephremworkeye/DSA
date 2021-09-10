class Stack:
    def __init__(self):
        self.stack = []
        self.min_value = []
        self.max_value = []
    def push(self, val): # return None
        if not self.stack:
            self.stack.append(val)
            self.min_value.append(val)
            self.max_value.append(val)
        else:
            self.stack.append(val)
            # if vlaue is greater than last element of max_value
            if val > self.max_value[-1]:
                self.max_value.append(val)
                self.min_value.append(self.min_value[-1])
            # if value is smaller than last element of min_value
            elif val < self.min_value[-1]:
                self.min_value.append(val)
                self.max_value.append(self.max_value[-1])
            # if value is between min_value and max-value
            else:
                self.min_value.append(self.min_value[-1])
                self.max_value.append(self.max_value[-1])

    
    def pop(self): #return None
        if self.stack:
            self.stack.pop()
            self.min_value.pop()
            self.max_value.pop()
        else:
            print('Stack is empty')


    def top(self): # return int
        if self.stack:
            return self.stack[-1]

    def get_min(self): # return int
        if self.min_value:
            return self.min_value[-1]
    
    def get_max(self):
        if self.max_value:
            return self.max_value[-1]
    


min_value = 6
last_min_value = 5

# value = 2, 5, 1, -1, 0, -2, -3
# stack = []
# max_value = [2, 5, 5, 5, 5, 5, 5, 9 ]
# min_value = [2, 2, 1, -1, -1, -2, -2]
# pop 9 

stack1 = Stack()
stack1.push(5)
stack1.push(3)
stack1.push(7)
stack1.push(2)
stack1.push(-1)
stack1.push(0)
stack1.push(10)
print(f'current maximum value: {stack1.get_max()}')
print(f'current minimum value: {stack1.get_min()}')
stack1.pop()
stack1.get_max()
stack1.get_min()
print(f'current maximum value: {stack1.get_max()}')
print(f'current minimum value: {stack1.get_min()}')