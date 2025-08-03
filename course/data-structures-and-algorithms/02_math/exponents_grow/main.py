def get_follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type == "fitness":
        r = 4
    elif influencer_type == "cosmetic":
        r = 3
    else:
        r = 2

    # geometric sequence formula
    prediction = follower_count * (r ** num_months)
    return prediction