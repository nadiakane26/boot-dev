def calculate_experience_points(level):
    current_xp = 0
    for i in range(1, level):
        current_xp += i * 5
    return current_xp