"""The COMP110-Sevier Collegiate Dictionary"""

__author__ = "730469212"


def invert(a: dict[str, str]) -> dict[str, str]:
    """flip-flops the keys and values of a dictionary"""
    invert_result: dict[str, str] = {}
    idx: int = 0
    while idx < len(a):
        new_key = list(a.keys())[idx]
        new_value = a[new_key]
        if new_value in invert_result:
            raise KeyError(f"Uh oh, duplicate value found: {new_value}")
        invert_result[new_value] = new_key
        idx += 1
    return invert_result


def count(b: list[str]) -> dict[str, int]:
    """counts the number of times a given value appears in a list"""
    count_result: dict[str, int] = {}
    for item in b:
        if item in count_result:
            count_result[item] += 1
        else:
            count_result[item] = 1
    return count_result


def favorite_color(c: dict[str, str]) -> str:
    """searches list of colors to find the color that appears the most"""
    colors: list[str] = list(c.values())
    color_count = count(colors)
    most_popular: str = ""
    max: int = 0
    for color in colors:
        if color_count[color] > max:
            max = color_count[color]
            most_popular = color

    return most_popular


def bin_len(d: list[str]) -> dict[int, set[str]]:
    """takes a list of strings and groups them based on their length"""
    len_result: dict[int, set[str]] = {}
    for word in d:
        if len(word) not in len_result:
            len_result[len(word)] = set()
        len_result[len(word)].add(word)
    return len_result
