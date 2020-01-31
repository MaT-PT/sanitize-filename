A simple, dependency-free, blacklist-based filename sanitizer, for when you want to keep the original filename.

Note that a blacklist based sanitizer will _never_ be as safe as a whitelist based one. In most cases, your best option is to create a safe filename yourself. Your second safest option is to use a whitelist approach (allowing only certain characters). This sanitizer is useful when you want to keep the original filename, including non ascii characters, whenever possible.

## Installation

```sh
pip install sanitize_filename
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

- 1.0.0-dev3

  - Black list low code point characters (<32)

- 1.0.0-dev1

  - First version