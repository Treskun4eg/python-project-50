from gendiff.modules.diff import diff
from gendiff.modules.formatter import format_to_strings
from gendiff.modules.open_file import open_file


def generate_diff(path1, path2):
    dict1 = open_file(path1)
    dict2 = open_file(path2)
    gen_diff = diff(dict1, dict2)
    format_to_string = format_to_strings(gen_diff)
    return format_to_string
