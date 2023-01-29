from gendiff.diff import diff
from gendiff.formatter import format_to_strings


def generate_diff(path1, path2):
    gen_diff = diff(path1, path2)
    format_to_string = format_to_strings(gen_diff)
    return format_to_string
