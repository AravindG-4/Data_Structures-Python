from collections import deque
import time
import threading

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]

service = Queue()
  
orders = ['pizza','samosa','pasta','biryani','burger']

def order(arr):
    for i in arr:
        service.enqueue(i)
        print("Placed order :",i)
        time.sleep(0.5)
        
def serve():
    time.sleep(1)
    while not service.is_empty():
        print("Served order :",service.dequeue())
        time.sleep(2)
        
def binary(n):
    service.enqueue('1')
    for i in range(n):
        a = service.front()
        service.enqueue(a+'0')
        service.enqueue(a+'1')
        
        print(service.dequeue())  

binary(10)