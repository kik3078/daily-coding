#Implement a job scheduler which takes in a function f and an integer n, 
#and calls f after n milliseconds.

import threading
import time

def delay(f, n):
    time.sleep(n)
    return f()

def print_test(text):
    print(text)
    
task = threading.Thread(target=delay, args=(lambda: print_test('Hello World!'), 0.01))
task.start()

# Threading example code

import threading
 
def doubler(number):
    
    print(threading.currentThread().getName() + '\n')
    print(number * 2)
    print()
 
 
if __name__ == '__main__':
    for i in range(5):
        my_thread = threading.Thread(target=doubler, args=(i,))
        my_thread.start()