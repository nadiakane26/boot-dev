# from main import *

# run_cases = [
#     (500, 1000, "incorrect amount"),
#     (800, 800, "correct amount"),
# ]

# submit_cases = run_cases + [
#     (1500, 1000, "incorrect amount"),
#     (200, 200, "correct amount"),
# ]


# def test(input1, input2, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {input1}, {input2}")
#     print(f"Expecting: {expected_output}")
#     result = check_swords_for_army(input1, input2)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False


# def main():
#     passed = 0
#     failed = 0
#     skipped = len(submit_cases) - len(test_cases)
#     for test_case in test_cases:
#         correct = test(*test_case)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")

#     if skipped > 0:
#         print(f"{passed} passed, {failed} failed, {skipped} skipped")
#     else:
#         print(f"{passed} passed, {failed} failed")


# test_cases = submit_cases
# if "__RUN__" in globals():
#     test_cases = run_cases

# main()

# L6 If-Else
# from main import *

# run_cases = [
#     (0, "dead"),
#     (4, "injured"),
# ]

# submit_cases = run_cases + [
#     (6, "healthy"),
#     (5, "injured"),
#     (1, "injured"),
#     (10, "healthy"),
#     (-1, "dead"),
# ]


# def test(health, expected_status):
#     print("---------------------------------")
#     print(f"Health: {health}")
#     print(f"Expecting: {expected_status}")
#     result = player_status(health)
#     print(f"Result: {result}")
#     if result == expected_status:
#         print("Pass")
#         return True
#     print("Fail")
#     return False


# def main():
#     passed = 0
#     failed = 0
#     skipped = len(submit_cases) - len(test_cases)
#     for test_case in test_cases:
#         correct = test(*test_case)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")
#     if skipped > 0:
#         print(f"{passed} passed, {failed} failed, {skipped} skipped")
#     else:
#         print(f"{passed} passed, {failed} failed")


# test_cases = submit_cases
# if "__RUN__" in globals():
#     test_cases = run_cases

# main()

# L7 If-Else Practice
# from main import *

# run_cases = [
#     ("ash ketchum", "ash ketchum", "You are the highest scoring player!"),
#     ("brock", "ash ketchum", "You are not the highest scoring player!"),
# ]

# submit_cases = run_cases + [
#     ("misty", "brock", "You are not the highest scoring player!"),
#     ("", "", "You are the highest scoring player!"),
#     ("same", "same", "You are the highest scoring player!"),
# ]


# def test(input1, input2, expected_output):
#     print("---------------------------------")
#     print(f"Inputs: {input1}, {input2}")
#     print(f"Expecting: {expected_output}")
#     result = check_high_score(input1, input2)
#     print(f"Actual: {result}")
#     if result == expected_output:
#         print("Pass")
#         return True
#     print("Fail")
#     return False


# def main():
#     passed = 0
#     failed = 0
#     skipped = len(submit_cases) - len(test_cases)
#     for test_case in test_cases:
#         correct = test(*test_case)
#         if correct:
#             passed += 1
#         else:
#             failed += 1
#     if failed == 0:
#         print("============= PASS ==============")
#     else:
#         print("============= FAIL ==============")
#     if skipped > 0:
#         print(f"{passed} passed, {failed} failed, {skipped} skipped")
#     else:
#         print(f"{passed} passed, {failed} failed")


# test_cases = submit_cases
# if "__RUN__" in globals():
#     test_cases = run_cases

# main()

#L8 If-Else Practice
from main import *

run_cases = [
    ("ash ketchum", "ash ketchum", "brock", "high"),
    ("brock", "ash ketchum", "brock", "low"),
]

submit_cases = run_cases + [
    ("misty", "brock", "ash ketchum", "neither"),
    ("red", "red", "blue", "high"),
    ("blue", "red", "blue", "low"),
    ("green", "red", "blue", "neither"),
]


def test(
    player_name, high_scoring_player_name, low_scoring_player_name, expected_output
):
    print("---------------------------------")
    print(
        f"Player Name: {player_name}, High Scoring Player: {high_scoring_player_name}, Low Scoring Player: {low_scoring_player_name}"
    )
    print(f"Expecting: {expected_output}")
    result = check_high_score(
        player_name, high_scoring_player_name, low_scoring_player_name
    )
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
