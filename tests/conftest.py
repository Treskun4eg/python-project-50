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
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }


@pytest.fixture
def file2_dict():
    return {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }
