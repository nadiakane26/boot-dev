def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        # Move the current element to its correct position in the sorted part of the array
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1 
    return nums
