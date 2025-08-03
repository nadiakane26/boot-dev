def find_minimum(nums):
    minimum = float('inf')  # Set minimum to positive infinity
    if not nums:
        return None
    
    for num in nums:
        if num < minimum:
            minimum = num
            
    return minimum 

S = "Some original string"
R = ""
