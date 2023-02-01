import pathlib
import json
import yaml


def open_file(path):
    file_format = pathlib.Path(path).suffix
    if file_format == '.json':
        data = open(path)
        return json.load(data)
    elif file_format == '.yaml' or file_format == '.yml':
        data = pathlib.Path(path).read_text()
        return yaml.safe_load(data)
