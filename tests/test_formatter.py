import ast
import pytest
from gendiff.modules.formatters import stylish
from gendiff.modules.formatters import plain
from gendiff.modules.formatters import json


@pytest.fixture
def diff_example():
    with open('tests/fixtures/diff_result.txt', 'r') as result:
        diff_result = ast.literal_eval(result.read())
        return diff_result


def test_get_string():
    assert stylish.get_string({"key": "host", "timeout": 50}, "key", 1) == '    host: host'


def test_format_to_string(diff_example):
    with open('tests/fixtures/result_stylish.txt', 'r') as result:
        assert stylish.format_to_strings(diff_example) == result.read()


def test_plain_format(diff_example):
    with open('tests/fixtures/result_plain.txt', 'r') as result:
        assert plain.plain_format(diff_example) == result.read()


def test_json_format(diff_example):
    with open('tests/fixtures/result_json.txt') as result:
        assert json.json_format(diff_example) == result.read()


def test_style_the_value():
    assert stylish.style_the_value({'a': 234, 'b': True, 'c': 'value'}, 0) == '{\n' \
                                                                      '    a: 234\n' \
                                                                      '    b: true\n' \
                                                                      '    c: value\n' \
                                                                      '}'
