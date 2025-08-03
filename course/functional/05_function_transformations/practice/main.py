def get_filter_cmd(filter_one, filter_two):
    def filter_cmd(content, option="--one"):
        if option == "--one":
            content = filter_one(content)
        elif option == "--two":
            content = filter_two(content)
        elif option == "--three":
            content = filter_two(filter_one(content))
        else:
            raise ValueError("invalid option")
        return content

    return filter_cmd


# don't touch below this line


def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")

