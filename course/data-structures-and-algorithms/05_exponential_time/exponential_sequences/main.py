def exponential_growth(n, factor, days):
    day_lists = []
    for day in range(days + 1):
        day_lists.append(n * (factor ** day)) # geometric progression
    return day_lists
