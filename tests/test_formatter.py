
from gendiff.formatter import style_the_value
from gendiff.formatter import get_string

file1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False,
    "nested": {
        "bool": True,
        "None": None,
        "string": "test string"
        }
    }


test_dict = {
    "proxy":
        {
            "key": "proxy",
            "value": "123.234.53.22",
            "operation": "added"
        }
}


def test_style_the_value():
    for key, value in file1.items():
        if isinstance(value, dict):
            assert style_the_value(value, 1) == \
                   f'{"{"}\n' \
                   f'    bool: true\n' \
                   f'    None: null\n' \
                   f'    string: test string\n' \
                   f'  {"}"}'
        elif isinstance(value, bool):
            assert style_the_value(value, 1) == str(value).lower()
        elif value is None:
            assert style_the_value(value, 1) == 'null'
        else:
            assert style_the_value(value, 1) == str(value)


def test_get_string():
    for key, value in test_dict.items():
        if value["operation"] == "added":
            assert get_string(value, "value", 1, "+ ") == \
                   f'  + {value["key"]}: {value["value"]}'


#    def iterable_dict(dict, depth):
#        new_str = ''
#        for k, v in dict.items():
#            result = style_the_value(v, depth + 1)
#            new_str += f'\n{k}: {result}'
#        return new_str
#
#    print(iterable_dict(file1, 1))
