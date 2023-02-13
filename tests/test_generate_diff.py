import pytest
from gendiff.modules.generate_diff import generate_diff


parameters = [('path1_plain_json', 'path2_plain_json', 'stylish', 'tests/fixtures/result_example.txt'),
              ('path1_plain_yml', 'path2_plain_yml', 'stylish', 'tests/fixtures/result_example.txt'),
              ('path1_json', 'path2_json', 'stylish', 'tests/fixtures/result_stylish.txt'),
              ('path1_json', 'path2_json', 'plain', 'tests/fixtures/result_plain.txt'),
              ('path1_json', 'path2_json', 'json', 'tests/fixtures/result_json.txt'),
              ('path1_yml', 'path2_yml', 'stylish', 'tests/fixtures/result_stylish.txt'),
              ('path1_yml', 'path2_yml', 'plain', 'tests/fixtures/result_plain.txt'),
              ('path1_json', 'path2_json', 'json', 'tests/fixtures/result_json.txt')]


@pytest.mark.parametrize('path1, path2, format, expected', parameters)
def test_generate_diff(path1, path2, format, expected, request):
    path1 = request.getfixturevalue(path1)
    path2 = request.getfixturevalue(path2)
    with open(expected, 'r') as result:
        assert generate_diff(path1, path2, format) == result.read()
