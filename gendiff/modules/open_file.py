import pathlib


def open_file(path):
    file_format = pathlib.Path(path).suffix
    if file_format == '.json':
        format = '.json'
        with open(path, 'r') as file:
            data = file.read()
        return data, format
    elif file_format == '.yaml' or file_format == '.yml':
        format = '.yml'
        data = pathlib.Path(path).read_text()
        return data, format
