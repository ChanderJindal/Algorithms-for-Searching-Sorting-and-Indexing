from numpy.random import randint

def Binary_Search(arr,item,l,r):
    mid = l + (r-l)//2
    if arr[mid] == item:
        return mid
    if arr[mid] > item:
        return Binary_Search(arr,item,l,mid-1)
    if arr[mid] < item:
        return Binary_Search(arr,item,mid+1,r)
    return -1

if __name__ == "__main__":
    a = randint(0, 1000,1000)
    a = sorted(a)
    print(a)
    print(Binary_Search(a,a[0],0,len(a)-1))
