def remove_nonints(nums):
    integers = []
    for num in nums:
        if type(num) is int:
            integers.append(num)
    return integers