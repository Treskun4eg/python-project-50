import json
import yaml


def parse(data, format: str):
    if format == '.json':
        return json.loads(data, strict=False)
    elif format == '.yml':
        return yaml.safe_load(data)
