def power_set(input_set):
    if not input_set:
        return [[]]
    all_subsets = [[]]
    for element in input_set:
        subsets_with_element = []
        for subset in all_subsets:
            new_subset = subset + [element]
            subsets_with_element.append(new_subset)
        all_subsets.extend(subsets_with_element)
    return all_subsets
