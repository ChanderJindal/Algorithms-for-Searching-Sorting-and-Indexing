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

if __name__ == "__main__":
    arr = [1,4,45,75,2,4,44,130,434,22]
    print(arr)
    merge_sort(arr)
    print(arr)
