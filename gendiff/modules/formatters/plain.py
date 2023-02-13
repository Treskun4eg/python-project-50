def plain_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    return f"'{value}'"


def plain_format(diff_result: dict):

    def walk(node, path):
        result = ''
        for key, value in node.items():
            current_path = f"{path}{value['key']}"
            if value['operation'] == 'added':
                result += f"Property '{current_path}' was added {plain_value(value['value'])}\n"
            elif value['operation'] == 'changed':
                result += f"Property '{current_path}' was updated. From {plain_value(value['old'])} to {plain_value(value['new'])}\n"
            elif value['operation'] == 'deleted':
                result += f"Property {current_path} was removed\n"
            elif value['operation'] == 'nested':
                result += walk(value['value'], current_path + '.') + '\n'
        return result[:-1]
    return walk(diff_result, '')
