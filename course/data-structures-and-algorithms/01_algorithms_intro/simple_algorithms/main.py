def sum(nums):
  # Recursive function to calculate the sum of a list of numbers
    # if not nums:
    #     return 0
    # return nums[0] + sum(nums[1:])

    # Iterative function to calculate the sum of a list of numbers
    sum = 0
    for num in nums:
        sum += num
    return sum