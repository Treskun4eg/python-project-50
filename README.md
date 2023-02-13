### Hexlet tests and linter status:
[![Maintainability](https://api.codeclimate.com/v1/badges/a1336332ffaafd2118c6/maintainability)](https://codeclimate.com/github/Treskun4eg/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a1336332ffaafd2118c6/test_coverage)](https://codeclimate.com/github/Treskun4eg/python-project-50/test_coverage)
[![gendiff_check](https://github.com/Treskun4eg/python-project-50/actions/workflows/gendiff_check.yml/badge.svg)](https://github.com/Treskun4eg/python-project-50/actions/workflows/gendiff_check.yml)

The package contains the program that outputs the differences between two files (JSON or YAML) in several possible formats. Available formats: stylish (default), plain, json.

### Installation

* Git clone:
```
git clone https://github.com/Treskun4eg/python-project-49.git
```
* Installation Poetry:
```
poetry install
```
* Project build:
```
poetry build
```
* Publication debugging:
```
poetry publish --dry-run
```
* Package-install:
```
python3 -m pip install --user dist/*.whl
```
* Reinstalling packages:
```
python3 -m pip install --upgrade --force-reinstall dist/hexlet_code-0.1.0-py3-none-any.whl
```

### After installation, the utility is used through the command:
```
gendiff --format <path/to/file1> <path/to/file2>
```

## Askinema with an example of how the package works:
### Simple file comparison example:
* [![asciicast](https://asciinema.org/a/555594.svg)](https://asciinema.org/a/555594)  
* [![asciicast](https://asciinema.org/a/557868.svg)](https://asciinema.org/a/557868)
### --format "stylish"
[![asciicast](https://asciinema.org/a/558097.svg)](https://asciinema.org/a/558097)
### --format "plain"
[![asciicast](https://asciinema.org/a/559616.svg)](https://asciinema.org/a/559616)
### --format "json"
[![asciicast](https://asciinema.org/a/559617.svg)](https://asciinema.org/a/559617)