# import randint to generate list of random integers
#from random import randint
import time
from numpy.random import randint
import matplotlib.pyplot as plt

#Heap Sort
def heapify(arr,length, i):
	largest = i # Initialize largest as root
	left = 2 * i + 1	 # left is 2n + 1
	right = 2 * i + 2	 # right is 2n + 2

    #left root is exists and is greater than initial greater
	if left < length and arr[largest] < arr[left]:
		largest = left

	#right root is exists and is greater than initial greater
	if right < length and arr[largest] < arr[right]:
		largest = right

	#since we changed largest, root node is changed too
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]

		# recheck
		heapify(arr,length, largest)


def heap_sort(arr):
    length = len(arr)
    for i in range( length//2 -1,-1,-1): # heapifying the half with roots
        heapify(arr,length,i)
    for i in range(len(arr)-1,0,-1): #heapifying the 2nd half after swaps
        arr[i] , arr[0] = arr[0] , arr[i]
        heapify(arr,i,0)

#Merge Sort
def merge_sort(arr):
    if len(arr) > 1: #make sure it isn't just 1 element
        mid = len(arr)//2 # divide it in 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right) # sort each half
        l = r = m = 0
        while l < len(left) and r < len(right): # from 2 sorted halfs, rebuild the original array by choosing the smaller elements
            if left[l] < right[r]:
                arr[m] = left[l]
                l += 1
            else:
                arr[m] = right[r]
                r += 1
            m += 1
        while l < len(left): # if any elements left in left, add them 
            arr[m] = left[l]
            l += 1
            m += 1
        while r < len(right):  # if any elements left in right, add them 
            arr[m] = right[r]
            m += 1
            r += 1

def insertion_sort(arr):
    for i in range(1,len(arr)):
        val = arr[i] # taking an element val
        j = i - 1
        while j > 0 and val < arr[j]: # searching an element less than val and swapping it
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val

#Quick Sort
def partition(start,end,arr):
    pvt_idx = start #initially taking the starting idx as partition idx, it can be end , mid or rand()
    pvt = arr[pvt_idx] # pivot element

    while start < end:
        while start < len(arr) and arr[start] <= pvt:# making sure all elements before pvt ele are smaller than equal to it
            start += 1
        
        while arr[end] > pvt:# making sure all elements after pvt ele are larger than it
            end -= 1
        
        #pre-sorted sub-arrays so to speak have been identified 

        if start < end: # if un-sorted parts remain 
            arr[start] , arr[end] = arr[end] , arr[start] #swap
        
    # continue the cycle

    arr[end], arr[pvt_idx] = arr[pvt_idx], arr[end] 
    #in the end pvt_idx is next to end, 
    return end # returning the pre-swapped pvt_idx

def quick_sort(start,end,arr):
    if start < end:
        p = partition(start,end,arr)# It's divide and conquer, fid the partition idx and sort the 2 halfs

        quick_sort(start,p-1,arr)
        quick_sort(p+1,end,arr)

MINIMUM= 32
  
def find_minrun(n): 
  
    r = 0
    while n >= MINIMUM: 
        r |= n & 1
        n >>= 1
    return n + r 
  
def insertion_sorter(array, left, right): 
    for i in range(left+1,right+1):
        element = array[i]
        j = i-1
        while element<array[j] and j>=left :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = element
    return array
              
def merge(array, l, m, r): 
  
    array_length1= m - l + 1
    array_length2 = r - m 
    left = []
    right = []
    for i in range(0, array_length1): 
        left.append(array[l + i]) 
    for i in range(0, array_length2): 
        right.append(array[m + 1 + i]) 
  
    i=0
    j=0
    k=l

    while j < array_length2 and  i < array_length1: 
        if left[i] <= right[j]: 
            array[k] = left[i] 
            i += 1
  
        else: 
            array[k] = right[j] 
            j += 1
  
        k += 1
  
    while i < array_length1: 
        array[k] = left[i] 
        k += 1
        i += 1
  
    while j < array_length2: 
        array[k] = right[j] 
        k += 1
        j += 1
  
def tim_sort(array): 
    n = len(array) 
    minrun = find_minrun(n) 
  
    for start in range(0, n, minrun): 
        end = min(start + minrun - 1, n - 1) 
        insertion_sorter(array, start, end) 
   
    size = minrun 
    while size < n: 
  
        for left in range(0, n, 2 * size): 
  
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
            merge(array, left, mid, right) 
  
        size = 2 * size 

elements1 = list()
times1 = list()
elements2 = list()
times2 = list()
elements3 = list()
times3 = list()
elements4 = list()
times4 = list()
elements5 = list()
times5 = list()
elements6 = list()
times6 = list()

for i in range(1, 10):

    a = randint(0, 1000 * i,1000*i)

    elements1.append(len(a))
    start = time.clock()
    heap_sort(a)
    end = time.clock()
    times1.append(end-start)

    a = randint(0, 1000 * i,1000*i)
    start = time.clock()
    merge_sort(a)
    end = time.clock()
    elements2.append(len(a))
    times2.append(end-start)
	
    a = randint(0, 1000 * i,1000*i)
    start = time.clock()
    insertion_sort(a)
    end = time.clock()
    elements3.append(len(a))
    times3.append(end-start)
	
    a = randint(0, 1000 * i,1000*i)
    start = time.clock()
    quick_sort(0,len(a)-1,a)
    end = time.clock()
    elements4.append(len(a))
    times4.append(end-start)

    a = randint(0, 1000 * i,1000*i)
    start = time.clock()
    tim_sort(a)
    end = time.clock()
    elements5.append(len(a))
    times5.append(end-start)

    a = randint(0, 1000 * i,1000*i)
    start = time.clock()
    sorted(a)
    end = time.clock()
    elements6.append(len(a))
    times6.append(end-start)

plt.xlabel('List Length')
plt.ylabel('Time Complexity')
plt.plot(elements1, times1, label ='Heap Sort')
plt.plot(elements2, times2, label ='Merge Sort')
plt.plot(elements3, times3, label ='Insertion Sort')
plt.plot(elements4, times4, label ='Quick Sort')
plt.plot(elements5, times5, label ='Tim Sort')
plt.plot(elements6, times6, label ='In-built Sort')
plt.grid()
plt.legend()
plt.show()    
