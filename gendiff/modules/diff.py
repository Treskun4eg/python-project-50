def common_and_different(dict1, dict2):
    added_keys = dict2.keys() - dict1.keys()
    deleted_keys = dict1.keys() - dict2.keys()
    common_keys = dict1.keys() & dict2.keys()
    return added_keys, deleted_keys, common_keys


def diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    added_keys, deleted_keys, common_keys = common_and_different(dict1, dict2)
    new_dict = {}
    for key in keys:
        if key in added_keys:
            description = {'key': key,
                           'value': dict2[key],
                           'operation': 'added'}
            new_dict[key] = description
        elif key in deleted_keys:
            description = {'key': key,
                           'value': dict1[key],
                           'operation': 'deleted'}
            new_dict[key] = description
        elif key in common_keys and dict1[key] == dict2[key]:
            description = {'key': key,
                           'value': dict1[key],
                           'operation': 'unchanged'}
            new_dict[key] = description
        elif all([key in common_keys,
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
