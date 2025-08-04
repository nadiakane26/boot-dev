def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    sorted_left_side = merge_sort(nums[:mid])
    sorted_right_side = merge_sort(nums[mid:])
    return merge(sorted_left_side, sorted_right_side)

# https://www.w3schools.com/python/python_dsa_mergesort.asp
def merge(left, right):
  result = []
  i = j = 0 # They will be used to keep track of indexes in the input lists (A and B).

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

