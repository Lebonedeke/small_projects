def binary_search(arr,target):
    
    start = 0
    end = len(arr) -1
    
    while start<= end:
        
        mid = start + end // 2
        
        if  arr[mid] == target:
            print('found at position', + mid +1)
            break
            
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    
mylist = [2,0,1,8,3,6,4]
find = 8

binary_search(mylist,find)