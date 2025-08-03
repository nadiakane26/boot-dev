# def check_swords_for_army(number_of_swords, number_of_soldiers):
#     if number_of_swords == number_of_soldiers:
#         return "correct amount"  

#     else:  
#         return "incorrect amount"

# # L6 If-Else
# def player_status(health):
#     if health <= 0:
#         return "dead"
#     elif health <= 5:
#         return "injured"
#     else:
#         return "healthy"

# L7 If-Else Practice
# def check_high_score(current_player_name, high_scoring_player_name):
#     if current_player_name == high_scoring_player_name:
#         return "You are the highest scoring player!"
#     else:
#         return "You are not the highest scoring player!"

# L8 If-Else Practice
def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"
