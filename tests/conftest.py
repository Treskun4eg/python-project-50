import pytest


@pytest.fixture
def file1():
    return {'a': 234, 'b': True, 'c': 'value'}


@pytest.fixture
def file2():
    return {'a': 234, 'b': False, 'd': None}


@pytest.fixture
def path1_plain_json():
    return 'tests/fixtures/file1_example.json'


@pytest.fixture
def path2_plain_json():
    return 'tests/fixtures/file2_example.json'


@pytest.fixture
def path1_plain_yml():
    return 'tests/fixtures/file1_example.yml'


@pytest.fixture
def path2_plain_yml():
    return 'tests/fixtures/file2_example.yml'


@pytest.fixture
def path1_json():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def path2_json():
    return 'tests/fixtures/file2.json'


@pytest.fixture
def path1_yml():
    return 'tests/fixtures/filepath1.yml'


@pytest.fixture
def path2_yml():
    return 'tests/fixtures/filepath2.yml'


@pytest.fixture
def file1_dict():
    return {
        'common': {
            'setting1': 'Value 1',
            'setting2': 200,
            'setting3': True,
            'setting6': {
                'key': 'value',
                'doge': {'wow': ''}
            }
        },
        'group1': {
            'baz': 'bas',
            'foo': 'bar',
            'nest': {'key': 'value'}
        },
        'group2': {
            'abc': 12345,
            'deep': {'id': 45}
        }
    }


@pytest.fixture
def file2_dict():
    return {
        'common': {
            'follow': False,
            'setting1': 'Value 1',
            'setting3': None,
            'setting4': 'blah blah',
            'setting5': {'key5': 'value5'},
            'setting6': {
                'key': 'value',
                'ops': 'vops',
                'doge': {'wow': 'so much'}
            }
        },
        'group1': {
            'foo': 'bar',
            'baz': 'bars',
            'nest': 'str'
        },
        'group3': {
            'deep': {
                'id': {'number': 45}
            },
            'fee': 100500
        }
    }
