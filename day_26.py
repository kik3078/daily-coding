#Given a singly linked list and an integer k, 
#remove the kth last element from the list. 
#k is guaranteed to be smaller than the length of the list.
#The list is very long, so making more than one pass is prohibitively expensive.
#
#Do this in constant space and in one pass.

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        current_node = self.head
        result = []
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return str(result)
    
    def append_after(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def remove_kth_from_tail(self, k):
        if self.head is None:
            return -1
        slow, fast = self.head, self.head
        for _ in range(k):
            fast = fast.next
        
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            
        prev.next = slow.next
        
    def remove_kth_from_head(self, k):
        if self.head is None:
            return -1
        cur_idx = 1
        prev = None
        cur_node = self.head
        while True:
            if cur_idx == k:
                if prev:
                    prev.next = cur_node.next
                else:
                    self.head = cur_node.next
                return True
            prev = cur_node
            cur_node = cur_node.next
            cur_idx += 1
                
    def reverse(self):
        prev = None
        head = self.head
        while head is not None: 
            temp = head
            head = head.next 
            temp.next = prev
            prev = temp
        self.head = prev

ll = LinkedList()
ll.append_after(1)
ll.append_after(2)
ll.append_after(3)
ll.append_after(4)
ll.append_after(5)

print(ll)
ll.remove_kth_from_tail(1)
print(ll)

ll2 = LinkedList()

ll2.append_after(1)
ll2.append_after(2)
ll2.append_after(3)
ll2.append_after(4)
ll2.append_after(5)

print(ll2)
ll2.reverse()
print(ll2)

ll2.remove_kth_from_head(5)
print(ll2)