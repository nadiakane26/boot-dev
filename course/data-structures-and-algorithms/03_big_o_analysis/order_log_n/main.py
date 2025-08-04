def binary_search(target, arr):
    """
    Perform a binary search on a sorted array to find the index of the target value.
    
    :param target: The value to search for.
    :param arr: A sorted list of integers.
    :return: The index of the target in the array, or -1 if not found.
    """
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return False
