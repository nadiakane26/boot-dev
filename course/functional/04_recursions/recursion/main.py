def factorial_r(x):
    if x < 2:
        return 1
    else:
        return x * factorial_r(x - 1)