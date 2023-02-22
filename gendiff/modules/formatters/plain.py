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


def plain_format(diff_result: dict): # noqa C901

    def walk(node, path):
        list_result = []
        for key, value in node.items():
            current_path = f"{path}{value['key']}"
            if value['operation'] == 'added':
                string = f"Property '{current_path}'" \
                         f" was added with value:" \
                         f" {plain_value(value['value'])}"
                list_result.append(string)
            elif value['operation'] == 'changed':
                string = f"Property '{current_path}' was updated." \
                         f" From {plain_value(value['old'])}" \
                         f" to {plain_value(value['new'])}"
                list_result.append(string)
            elif value['operation'] == 'deleted':
                string = f"Property '{current_path}' was removed"
                list_result.append(string)
            elif value['operation'] == 'nested':
                string = walk(value['value'], current_path + '.')
                list_result.append(string)
        return '\n'.join(list_result)
    return walk(diff_result, '')
