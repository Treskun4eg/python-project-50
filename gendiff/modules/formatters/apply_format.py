from gendiff.modules.formatters.stylish import format_to_strings


def apply_format(diff_result, format='stylish'):
    if format == 'stylish':
        return format_to_strings(diff_result)
