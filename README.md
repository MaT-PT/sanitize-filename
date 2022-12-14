_Forked from [GitLab](https://gitlab.com/jplusplus/sanitize-filename)_

A simple, dependency-free, blacklist-based filename sanitizer, for when you want to keep the original filename.

Note that a blacklist based sanitizer will _never_ be as safe as a whitelist based one. In most cases, your best option is to create a safe filename yourself. Your second safest option is to use a whitelist approach (allowing only certain characters). This sanitizer is useful when you want to keep the original filename, including non ascii characters, whenever possible.

## Installation

```sh
pip install -U git+https://github.com/MaT-PT/sanitize-filename.git#egg=sanitize_filename

-or-

pip install -U https://github.com/MaT-PT/sanitize-filename/tarball/master#egg=sanitize_filename
```

## Usage

```python3
from sanitize_filename import sanitize


filename = input("Enter a file name:")
filename = sanitize(filename)
```

Examples:

```python3
> sanitize("A/B/C.txt")
'ABC.txt'

> sanitize("this𓀦filenameḜisあactually...valid.txt")
'this𓀦filenameḜisあactually...valid.txt'

> sanitize("def.")
'def'

> sanitize("NUL")
'__NUL'

> sanitize("..")
'__'
```

## Changelog

- 1.2.2

  - Add option to choose a replacement string for illegal characters
  - Check reserved Windows file names in a case-insensitive manner
  - Update pip command in README to use this GitHub repo

- 1.2.1

  - Add Python type hints
  - Fix setup.py: use UTF-8 encoding when opening README.md

- 1.2.0

  - Get rid of os dependent checks; ensure uniform behaviour
  - Now works on long filenames where the non-extensions part consists of only dots

- 1.1.0

  - Try to preserve filename extensions if possible

- 1.0.1

  - First release (as 1.0.1 due to a version number mix-up in 1.0.0)

- 1.0.0-dev3

  - Black list low code point characters (<32)

- 1.0.0-dev1

  - First version