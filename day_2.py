# Given an array of integers, return a new array such that 
# each element at index i of the new array is the product 
# of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected
# output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
# the expected output would be [2, 3, 6].
# Follow-up: what if you can't use division?

input_list = [1, 2, 3, 4, 5]


result = []

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __is_empty(self):
        if not self.head:
            return True
        
        return False  
      
    def enqueue(self, data):
        new_node = Node(data)
        
        if self.__is_empty():
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node
    
    def __length(self):
        cur = self.head
        total = 1
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def get(self, index):
        if index >= self.__length() or index < 0:
            print("Error")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            if cur_idx == index:
                return cur_node.data
            cur_node = cur_node.next
            cur_idx += 1
        
    def dequeue(self):
        if self.__is_empty():
            return None
        
        ret_data = self.head.data
        self.head = self.head.next
        return ret_data
    
my_q = Queue()
[my_q.enqueue(input_list[i]) for i in range(len(input_list))]
tmp_products = 1

for i in range(len(input_list)):
    ret_data = my_q.dequeue()
    for i in range(len(input_list) - 1):
        tmp_products *= my_q.get(i)
    result.append(tmp_products)
    tmp_products = 1
    my_q.enqueue(ret_data)
    
print(result)