def find_min(nums):
    smallest_number = float("inf")
    for num in nums:
        if num < smallest_number:
            smallest_number = num
    return smallest_number