def merge(dict1, dict2):
   # https://www.geeksforgeeks.org/python-merging-two-dictionaries/
   # return dict1 | dict2  # Using the union operator to merge two dictionaries in Python 3.9+.

      # Update the copy with dict2
    return dict1.update(dict2)          # Return the merged dictionary