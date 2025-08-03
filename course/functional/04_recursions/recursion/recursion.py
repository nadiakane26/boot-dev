d = { # 3 layers
    "melee_weapons": { # First level, corresponds to single dictionary, only key
        "stabbies":{ # Second level, corresponds 2 keys: stabbies and bows
            "spears": 4, # Third level, corresponds to 2 keys: spears, knives
            "knives": 3,
        },
        "bows": 6
    }
}
def dict_depth(d, max_depth_so_far = 0):
    """Recursively find the maximum depth of a nested dictionary."""
    if not isinstance(d, dict) or not d:
        return max_depth_so_far
    
    current_depth = max_depth_so_far 
    for v in d.values():
        depth_of_subdict = dict_depth(v, max_depth_so_far + 1)
        if depth_of_subdict > current_depth:
          current_depth = depth_of_subdict
    
    return current_depth


def print_chars(word, i):
    if i == len(word):
        return
    print(word[i])
    print_chars(word, i + 1)

print_chars("Elephant", 3)
# H
# e
# l
# l
# o