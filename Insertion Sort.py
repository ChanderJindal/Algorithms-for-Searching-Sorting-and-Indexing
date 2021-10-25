#Insertion Sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        val = arr[i] # taking an element val
        j = i - 1
        while j > 0 and val < arr[j]: # searching an element less than val and swapping it
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = val

if __name__ == "__main__":
    arr = [1,4,45,75,2,4,44,130,434,22]
    print(arr)
    insertion_sort(arr)
    print(arr)
