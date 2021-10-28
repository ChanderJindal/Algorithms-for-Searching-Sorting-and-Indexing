import random

from numpy.random.mtrand import rand

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
  
    def isEmpty(self):
        return len(self.queue) == 0
  
    def insert(self, data):
        self.queue.append(data)

    def top(self):
        if self.isEmpty() == True:
            print("NO elements in here")
            return
        max = 0
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[max]:
                max = i
        return self.queue[max]
  
    def delete(self):
        max = 0
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[max]:
                max = i
        item = self.queue[max]
        del self.queue[max]
        return item

  
if __name__ == '__main__':
    myQueue = PriorityQueue()
    print("Elements at Top are : ")
    for i in range(10):
        myQueue.insert( random.randint(0,100) )
        print(myQueue.top())
    print("My current Queue is : ",end="")
    print(myQueue.queue)    
    print("Elements while deleting the Queue")        
    while not myQueue.isEmpty():
        print(myQueue.delete()) 
