import math 

def num_possible_orders(num_posts):
    return math.factorial(num_posts)

    # product = 1
    # for i in range(1, num_posts + 1):
    #     product *= i
    # return product

