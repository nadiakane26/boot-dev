def find_max(nums):
    max_so_far = float("-inf")
    return max(max_so_far, *nums) if nums else max_so_far
