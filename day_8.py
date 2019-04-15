#A unival tree (which stands for "universal value") is a tree 
#where all nodes under it have the same value.
#Given the root to a binary tree, count the number of unival subtrees.
#For example, the following tree has 5 unival subtrees:
#
#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(self.root, data)
            
    def _add(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._add(node.left, data)
                
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._add(node.right, data)
                
    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
            
        else:
            print("The tree is empty!")
    
    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(node.data)
            self._printTree(node.right)
            
tree = BinaryTree()