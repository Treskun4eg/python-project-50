from gendiff.diff import generate_diff
from gendiff.formatter import format_to_strings


def gen_diff(path1, path2):
    diff = generate_diff(path1, path2)
    format_to_string = format_to_strings(diff)
    return format_to_string
