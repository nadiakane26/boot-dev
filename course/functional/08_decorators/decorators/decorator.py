def to_uppercase(func):
    def wrapper(document):
        return func(document.upper()) # document = "Keep Calm and Carry On".upper() → "KEEP CALM AND CARRY ON"

    return wrapper

def get_truncate(length):
    def truncate(func): # returns the inner `truncate(func)` decorator
        def wrapper(document): # which returns a `wrapper(document)` that calls `func(document[:9])`
            return func(document[:length]) # "KEEP CALM AND CARRY ON"[:9] → "KEEP CALM"

        return wrapper

    return truncate

@to_uppercase # print_input = to_uppercase(get_truncate(9)(print_input))
@get_truncate(9) # currying # print_input = get_truncate(9)(print_input)
def print_input(input):
    print(input)

print_input("Keep Calm and Carry On")
# prints: "KEEP CALM"