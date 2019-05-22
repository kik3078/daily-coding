#You are given an array of non-negative integers that 
#represents a two-dimensional elevation map 
#where each element is unit-width wall and the integer is the height. 
#Suppose it will rain and all spots between two walls get filled up.
#
#Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
#
#For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
#
#Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 
#2 in the second, and 3 in the fourth index 
#(we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.


stack = []
given = [3, 0, 1, 3, 0, 5]
water = 0

for val in given:
    if len(stack) == 1 and stack[0] <= val:
        stack.pop()
            
    stack.append(val)
    print(stack)
    
    if len(stack) >= 2:
        if stack[0] <= val:
            water += stack[0] * (len(stack) - 2) - sum([stack[i] for i in range(1, len(stack) - 1)])
            print("water : {0}".format(water))
            stack.clear()
            print(stack)
            stack.append(val)
            
print(water)