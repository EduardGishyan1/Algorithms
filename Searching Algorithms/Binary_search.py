# Iterative 

def BinarySearch(arr,target):
    high = len(arr) - 1
    low = 0
    
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1
        
        elif arr[mid] > target:
            high = mid - 1
            
# Recursive
            
def Binary_Search(arr,target,low,high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] < target:
        return Binary_Search(arr,target,mid + 1,high)
    
    elif arr[mid] > target:
        return Binary_Search(arr,target,low,mid - 1)