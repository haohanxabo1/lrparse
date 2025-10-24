# Lr Parse
## _Easy To Get The Substrings_


[![PyPI-version](https://img.shields.io/pypi/v/lrparse.svg)](https://pypi.org/project/lrparse/)
[![View on GitHub](https://img.shields.io/badge/GitHub-view-brightgreen?logo=github)](https://github.com/haohanxabo1/lrparse)

lrparse is a tiny, fast Python library written in C for extracting substrings between left and right delimiters.

## Features

- `lr()` — fetches the first occurrence between a left and right delimiter.

- `lrr()` — fetches all non-overlapping occurrences between delimiters.

- Returns results as native Python lists of strings for easy integration

## Install

```sh
pip install lrparse
```

## Usage

```python
import lrparse

# lr() → first match between delimiters
print(lrparse.lr("pre[mid]post", "[", "]"))
# Output: ['mid']

# lrr() → all matches between delimiters
print(lrparse.lrr("<a><b>c", "<", ">"))
# Output: ['a', 'b']

# If delimiters don't exist → returns an empty list
print(lrparse.lr("hello world", "{", "}"))
# Output: []

# If both delimiters are empty → returns the whole string
print(lrparse.lr("abc", "", ""))
# Output: ['abc']
```

## Shoutout
The idea behind this project came from the *Parse Block* in [OpenBullet](https://github.com/openbullet/openbullet/) - a powerful tool for automating and analyzing HTTP requests.
I always liked how fast and straightforward it handled text extraction, so I wanted to create a tiny standalone version for Python.  

Big respect to the OpenBullet devs and community. 🙌
