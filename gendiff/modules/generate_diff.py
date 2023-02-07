from gendiff.modules.diff import diff
from gendiff.modules.open_file import open_file
from gendiff.modules.formatters.apply_format import apply_format


def generate_diff(path1, path2, format='stylish'):
    dict1 = open_file(path1)
    dict2 = open_file(path2)
    gen_diff = diff(dict1, dict2)
    return apply_format(gen_diff, format)
