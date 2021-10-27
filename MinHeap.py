# Python3 implementation of Min Heap
import random

class MinHeap:

	def __init__(self, maxsize):
		
		self.maxsize = maxsize
		self.size = 0
		self.Heap = [0] * (self.maxsize + 1)
		self.Heap[0] = 0
		self.FRONT = 1

	def parent(self, pos): #parent is always position/2 (integeral)
		
		return pos // 2

	def leftChild(self, pos): # left child = 2*n , 1-based-indexing
		
		return 2 * pos

	def rightChild(self, pos): # right child = 2*n+1 , 1 - based-indexing
		
		return (2 * pos) + 1


	def isLeaf(self, pos):
		
		if pos >= (self.size//2) and pos <= self.size: # make sure it's not internal node and not out of bounds
			return True
		return False

	def swap(self, fpos, spos):
		
		self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],self.Heap[fpos])

	# Function to heapify the node at pos
	def minHeapify(self, pos):

		# If the node is a non-leaf node and smaller
		# than any of its child
		if not self.isLeaf(pos): # non-leaf 
			if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or self.Heap[pos] > self.Heap[self.rightChild(pos)]): #it has either a left or right child less than the parent so, swap is needed


				if (self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]):#left is lesser 
					self.swap(pos, self.leftChild(pos)) #swap left 
					self.maxHeapify(self.leftChild(pos)) # check the rest
				else: # right is lesser 
					self.swap(pos, self.rightChild(pos)) # swap right
					self.minHeapify(self.rightChild(pos)) #check rest

	# Function to insert a node into the heap
	def insert(self, element):
		
		if self.size >= self.maxsize: #no space left
			return
		self.size += 1 # making new space
		self.Heap[self.size] = element #adding new element

		current = self.size

		while (self.Heap[current] < self.Heap[self.parent(current)]): #if new element is greater than parent
			self.swap(current, self.parent(current)) # swap
			current = self.parent(current) # check the rest, by updating the current idx

	def Top(self): # finding the top

		popped = self.Heap[self.FRONT] #got the max element
		self.Heap[self.FRONT] = self.Heap[self.size] #replacing root with lowest order element
		self.size -= 1
		self.minHeapify(self.FRONT) # remaking heap with the root // Bubble down so to say
		
		return popped

# Driver Code
if __name__ == "__main__":

    heap = MinHeap(10)
    print("Elements in the Heap are :- ",end= " ")
    for i in range(10):
        temp = random.randint(0,100000)
        heap.insert(temp)
        print(temp,end=" ")

    print("\nThe current smallest element in MinHeap is :", heap.Top())
    


	
