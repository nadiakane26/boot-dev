def get_most_common_enemy(enemies_dict):
    if not enemies_dict:
        return None
    
    max_count = float("-inf")
    most_common_enenmy = None

    for enemy_name, count in enemies_dict.items():
        if count > max_count:
            max_count = count
            most_common_enenmy = enemy_name
    return most_common_enenmy