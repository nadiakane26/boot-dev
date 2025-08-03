def zipmap(keys, values):
    if not keys or not values:
        return {}
    rest = zipmap(keys[1:], values[1:]) 
    rest[keys[0]] = values[0] 
    return rest