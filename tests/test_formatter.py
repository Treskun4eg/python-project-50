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


@pytest.fixture
def style_example():
    with open('tests/fixtures/style_example.txt') as result:
        result_style = ast.literal_eval(result.read())
        return result_style


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


def test_style_the_value(style_example):
    with open('tests/fixtures/result_style_json.txt') as result:
        assert stylish.style_the_value(style_example, 0) == result.read()
