#Tim Sort
MIN_MERGE = 32
 
def calcMinRun(n): # it gives the min. possible run for size n, that is related to power of 2
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(arr,start,end):
    for i in range(start+1,end+1):
        val = arr[i] # taking an element val
        j = i - 1
        while j > start and val < arr[j]: # searching an element less than val and swapping it
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val

def merge_sort(arr, l, m, r):
    len1 , len2 = m-l+1,r-m #custom lengths 
    left , right = [] , []
    for i in range(0,len1):
        left.append(arr[l+i])
    for i in range(0,len2):
        right.append(arr[m+i+1]) # added respective values

        l , r , m = 0,0,l
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

def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
     
    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertion_sort(arr, start, end)
 
    size = minRun # starting the merge
    while size < n: # note size doubles everytime
         
        for left in range(0, n, 2 * size): # for left be one end
 
            mid = min(n - 1, left + size - 1) # mid be the point of division
            right = min((left + 2 * size - 1), (n - 1)) # right is other end of the sub-array
 
            if mid < right:
                merge_sort(arr, left, mid, right) # merging left to mid and mid to right
 
        size = 2 * size # ever increasing size


if __name__ == "__main__":
    arr = [1,4,45,75,2,4,44,130,434,22]
    print(arr)
    timSort(arr)
    print(arr)
