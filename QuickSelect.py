from numpy.random import randint

def partition(arr, l, r):
	
	x = arr[r]
	i = l
	for j in range(l, r):
		
		if arr[j] <= x:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
			
	arr[i], arr[r] = arr[r], arr[i]
	return i

def kthSmallest(arr, l, r, k):

	if (k > 0 and k <= r - l + 1): #make sure k is in range

		idx = partition(arr, l, r) # get a partition

		if (idx - l == k - 1): #idx same as k
			return arr[idx]

		if (idx - l > k - 1): # idx > k, look in left / lower half 
			return kthSmallest(arr, l, idx - 1, k) # i.e. l to idx -1 
        # idx < k , look in right / upper half
		return kthSmallest(arr, idx + 1, r,	k - idx + l - 1)#i.e. idx + 1 to r , also, from k we have eleminated l - idx elements
	print("Index out of bound")# outside the idx range

arr = randint(0,100,100)
n = len(arr)
k = randint(0,n)
print(k,"-th smallest element is ",sep="", end = "")
print(kthSmallest(arr, 0, n - 1, k))
