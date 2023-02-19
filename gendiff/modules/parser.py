import json
import yaml


def parse(data, format: str):
    if format == '.json':
        return json.load(data)
    elif format == '.yml':
        return yaml.safe_load(data)
