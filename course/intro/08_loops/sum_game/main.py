# def sum_of_numbers(start, end):
#     total = 0
#     for i in range(start, end):
#         total += i
#     return total

def sum_of_odd_numbers(end):
    total = 0
    for i in range(1, end, 2):
        total += i
    return total