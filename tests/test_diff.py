import ast
import pytest
from gendiff.modules.diff import compare_files, diff


def test_compare_files(file1, file2):
    added_key, deleted_key, common_key = compare_files(file1, file2)
    assert added_key == {"d"}
    assert deleted_key == {"c"}
    assert common_key == {"a", "b"}


parameters = [('file1', 'file2', 'tests/fixtures/diff_result_simple.txt'),
              ('file1_dict', 'file2_dict', 'tests/fixtures/diff_result.txt')]


@pytest.mark.parametrize('arg1, arg2, expected', parameters)
def test_diff(arg1, arg2, expected, request):
    arg1_value = request.getfixturevalue(arg1)
    arg2_value = request.getfixturevalue(arg2)
    with open(expected) as result:
        diff_resul = ast.literal_eval(result.read())
        assert diff(arg1_value, arg2_value) == diff_resul
