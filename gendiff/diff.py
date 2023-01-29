import json
import pathlib


def open_file(path):
    dir_file = pathlib.Path(path)
    open_file1 = open(dir_file)
    load_file = json.load(open_file1)
    return load_file


def compare_files(dict1, dict2):
    added_key = dict2.keys() - dict1.keys()
    deleted_key = dict1.keys() - dict2.keys()
    common_key = dict1.keys() & dict2.keys()
    return added_key, deleted_key, common_key


def diff(path1, path2):
    dict1 = open_file(path1)
    dict2 = open_file(path2)
    keys = sorted(dict1.keys() | dict2.keys())
    added_key, deleted_key, common_key = compare_files(dict1, dict2)
    new_dict = {}
    for key in keys:
        if key in added_key:
            description = {'key': key,
                           'value': dict2[key],
                           'operation': 'added'}
            new_dict[key] = description
        elif key in deleted_key:
            description = {'key': key,
                           'value': dict1[key],
                           'operation': 'deleted'}
            new_dict[key] = description
        elif key in common_key and dict1[key] == dict2[key]:
            description = {'key': key,
                           'value': dict1[key],
                           'operation': 'unchanged'}
            new_dict[key] = description
        elif all([key in common_key,
                  dict1[key] != dict2[key],
                  isinstance(dict1[key], dict),
                  isinstance(dict2[key], dict)]
                 ):
            description = {'key': key,
                           'value': diff(dict1[key], dict2[key]),
                           'operation': 'nested'}
            new_dict[key] = description
        else:
            description = {'key': key,
                           'old': dict1[key],
                           'new': dict2[key],
                           'operation': 'changed'}
            new_dict[key] = description
    return new_dict
