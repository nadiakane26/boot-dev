def get_estimated_spread(audiences_followers):
    if not audiences_followers:
        return 0

    average = sum(audiences_followers) / len(audiences_followers)
    multiplier = len(audiences_followers) ** 1.2
    return average * multiplier