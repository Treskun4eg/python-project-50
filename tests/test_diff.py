import json
import pytest
from gendiff.diff import open_file
from gendiff.diff import compare_files
from gendiff.diff import generate_diff


@pytest.fixture
def open_file1():
    return json.load(open('tests/fixtures/file1.json'))


@pytest.fixture
def open_file2():
    return json.load(open('tests/fixtures/file2.json'))


def test_open_file(open_file1):
    assert open_file('tests/fixtures/file1.json') == open_file1


def test_compare_files(open_file1, open_file2):
    dict1 = open_file1
    dict2 = open_file2
    compare_dictionaries = (
        dict2.keys() - dict1.keys(),
        dict1.keys() - dict2.keys(),
        dict1.keys() & dict2.keys()
    )
    assert compare_files(dict1, dict2) == compare_dictionaries


def test_generate_diff():
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    expected_tree = {
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

    assert generate_diff(path1, path2) == expected_tree
