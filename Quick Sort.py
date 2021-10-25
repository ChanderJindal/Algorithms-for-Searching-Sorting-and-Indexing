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

if __name__ == "__main__":
    arr = [1,4,45,75,2,4,44,130,434,22]
    print(arr)
    quick_sort(0,len(arr)-1,arr)
    print(arr)
