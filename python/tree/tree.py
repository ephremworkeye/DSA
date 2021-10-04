class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None


    #             7
    #          /    \
    #         4      10
    #        / \     / \
    #       2   6   8   15
    def insert(self, value):
        new_node = Node(value)
        # if empty
        if self.root == None:
            self.root = new_node
            return True
        current = self.root
        while True:
            # repeated value not allowed
            if new_node.value == current.value:
                return False
            if new_node.value < current.value:
                if current.left == None:
                    current.left = new_node
                    return True
                current = current.left
            else:
                if current.right == None:
                    current.right = new_node
                    return True
                current = current.right    

    def contain(self, value):
        if self.root == None:
            return False
        current = self.root
        while current:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return False



binary_tree = BinarySearchTree()
binary_tree.insert(7)
binary_tree.insert(10)
binary_tree.insert(4)
binary_tree.insert(2)
binary_tree.insert(8)
binary_tree.insert(15)
binary_tree.insert(6)

print(binary_tree.contain(2))

# print(binary_tree.root.value)
# print(binary_tree.root.left.value)
# print(binary_tree.root.right.value)

        
