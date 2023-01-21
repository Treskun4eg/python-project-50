import itertools


def style_the_value(value, depth):
    if isinstance(value, dict):
        string = ''
        for key, value in value.items():
            space = '  ' * (depth + 1)
            string += f"\n{space}{key}: {style_the_value(value, depth + 1)}"
        concatenate_string = itertools.chain(
            '{', string, '\n', ['  ' * depth, '}']
        )
        return ''.join(concatenate_string)
    else:
        if isinstance(value, bool):
            return str(value).lower()
        elif value is None:
            return 'null'
        else:
            return str(value)


def get_string(dictionary, key, depth, sign='  '):
    string = f'{"  " * depth}{sign}{dictionary["key"]}: '\
             f'{style_the_value(dictionary[key], depth + 1)}'
    return string


def format_to_strings(diff_result): # noqa C901

    def walk(node, depth, replace='  '):
        string = ''
        space = replace * (depth + 1)
        for k, v in node.items():
            if v['operation'] == 'nested':
                string += f'\n{space*2}{v["key"]}: {walk(v["value"], depth+1)}'
            elif v['operation'] == 'added':
                string += f'\n{space}{get_string(v, "value", depth, "+ ")}'
            elif v['operation'] == 'changed':
                string += f'\n{space}{get_string(v, "old", depth, "- ")}'
                string += f'\n{space}{get_string(v, "new", depth, "+ ")}'
            elif v['operation'] == 'unchanged':
                string += f'\n{space}{get_string(v, "value", depth)}'
            elif v['operation'] == 'deleted':
                string += f'\n{space}{get_string(v, "value", depth, "- ")}'
        result = itertools.chain('{', string, '\n', ['  ' * depth + '}'])
        return ''.join(result)

    return walk(diff_result, 0)
