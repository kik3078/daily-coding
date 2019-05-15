#Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).
#
#For example, given the string "([])[]({})", you should return true.
#
#Given the string "([)]" or "((()", you should return false.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        if self.head is None:
            return True
        
        return False
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
            
    def pop(self):
        if self.is_empty():
            return None
        
        ret_data = self.head.data
        self.head = self.head.next
        
        return ret_data
    
    def peek(self):
        if self.is_empty():
            return None
        
        return self.head.data
    
#given = ['(', '[', ']', ')', '[', ']', '(', '{', '}', ')']
given = ['(', ')']

def check(given):
    stack = Stack()
    for char in given:
        if char in ['(', '[', '{']:
            stack.push(char)
            
        else:
            if not stack:
                return False
            
            if char == ')' and stack.head.data != '(' or \
               char == ']' and stack.head.data != '[' or \
               char == '}' and stack.head.data != '{':
                   print(stack.peek())
                   return False
            stack.pop()
        
    return stack.is_empty()

print(check(given))