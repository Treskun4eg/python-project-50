from gendiff.generate_diff import gen_diff


def test_gen_diff():
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    expected = '{\n' \
               '  - follow: false\n' \
               '    host: hexlet.io\n' \
               '  - proxy: 123.234.53.22\n' \
               '  - timeout: 50\n' \
               '  + timeout: 20\n' \
               '  + verbose: true\n' \
               '}'
    assert gen_diff(path1, path2) == expected