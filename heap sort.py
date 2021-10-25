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


if __name__ == "__main__":
    arr = [1,4,45,75,2,4,44,130,434,22]
    print(arr)
    heap_sort(arr)
    print(arr)
