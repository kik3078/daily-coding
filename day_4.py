#Given an array of integers, find the first missing positive integer 
#in linear time and constant space. In other words, 
#find the lowest positive integer that does not exist in the array. 
#The array can contain duplicates and negative numbers as well.
#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#You can modify the input array in-place.

input_list = [3, 4, -1, 1]
input_list = [1, 2, 0]
input_list.sort()
# -1 1 3 4
def find_positive_min(input_list):
    for i in range(len(input_list)):
        if input_list[i] >= 0:
           return i
       
    return -1

def answer(input_list):
    index = find_positive_min(input_list)
    if index == -1:
        return -1
    elif index == len(input_list) - 1:
        return input_list[index] + 1
    
    while True:
        if input_list[index + 1] - input_list[index] >= 2:
            return input_list[index] + 1
        else:
            index += 1
            if index + 1 == len(input_list):
                if input_list[index] < 0:
                    return - 1
                else:
                    return input_list[index] + 1
    
print(answer(input_list))