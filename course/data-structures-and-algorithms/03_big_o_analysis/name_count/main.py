def count_names(list_of_lists, target_name):
    count = 0
    for lists in list_of_lists:
        for name in lists:
            if name == target_name:
                count += 1
    return count

