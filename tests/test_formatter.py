import json
import pytest
from gendiff.formatter import style_the_value
from gendiff.formatter import get_string
from gendiff.formatter import format_to_strings


@pytest.fixture
def open_file3():
    return json.load(open('tests/fixtures/file3.json'))


@pytest.fixture
def open_file4():
    return json.load(open('tests/fixtures/file4.json'))


def test_style_the_value(open_file3):
    for key, value in open_file3.items():
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


def test_get_string(open_file4):
    for key, value in open_file4.items():
        if value["operation"] == "added":
            assert get_string(value, "value", 1, "+ ") == \
                   f'  + {value["key"]}: {value["value"]}'


def test_format_to_strings():
    diff_result = {
        'follow':
            {
                'key': 'follow',
                'value': False,
                'operation': 'deleted'
            },
        'host':
            {
                'key': 'host',
                'value': 'hexlet.io',
                'operation': 'unchanged'
            },
        'proxy':
            {
                'key': 'proxy',
                'value': '123.234.53.22',
                'operation': 'deleted'
            },
        'timeout':
            {
                'key': 'timeout',
                'old': 50,
                'new': 20,
                'operation': 'changed'
            },
        'verbose':
            {
                'key': 'verbose',
                'value': True,
                'operation': 'added'
            }
    }
    expected = '{\n' \
               '  - follow: false\n' \
               '    host: hexlet.io\n' \
               '  - proxy: 123.234.53.22\n' \
               '  - timeout: 50\n' \
               '  + timeout: 20\n' \
               '  + verbose: true\n' \
               '}'
    assert format_to_strings(diff_result) == expected
