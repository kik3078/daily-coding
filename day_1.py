given_list = [10, 15, 3, 7]

target = 17
given_list.sort()

def check(given_list):
    a = 0
    k = len(given_list) - 1
    while(a < k):
        if given_list[a] + given_list[k] == target:
            return True
        elif given_list[a] + given_list[k] > target:
            k -= 1
        elif given_list[a] + given_list[k] < target:
            a += 1
            
    return -1

print(check(given_list))