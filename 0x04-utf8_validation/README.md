# 0x04. UTF-8 Validation

## Overview

This project, "0x04. UTF-8 Validation," focuses on developing a method to validate UTF-8 encoded data using Python. It requires applying knowledge of bitwise operations, understanding the UTF-8 encoding scheme, and proficiency in Python programming. The goal is to determine whether a given dataset represents a valid UTF-8 encoding.

## Project Details

- **Project Start Date:** May 20, 2024, 6:00 AM
- **Project End Date:** May 24, 2024, 6:00 AM
- **Checker Release Date:** May 21, 2024, 6:00 AM
- **Auto Review:** An automatic review will be conducted at the deadline.

## Concepts Needed

To successfully complete this project, the following concepts are essential:

### Bitwise Operations in Python

- Understanding how to manipulate bits in Python, including operations like AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), and shifts (`<<`, `>>`).
- [Python Bitwise Operators](https://realpython.com/python-bitwise-operators/)

### UTF-8 Encoding Scheme

- Familiarity with UTF-8 encoding rules, including how characters are encoded into one or more bytes.
- Understanding the patterns that represent a valid UTF-8 encoded character.
- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

### Data Representation

- How to represent and work with data at the byte level.
- Handling the least significant bits (LSB) of integers to simulate byte data.

### List Manipulation in Python

- Iterating through lists, accessing list elements, and understanding list comprehensions.
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

### Boolean Logic

- Applying logical operations to make decisions within the program.

## Additional Resource

- [Mock Technical Interview](https://www.pramp.com/)

## Requirements

- **Allowed Editors:** `vi`, `vim`, `emacs`
- **Interpreter/Compiler:** Python 3.4.3 on Ubuntu 20.04 LTS
- **File Requirements:**
  - All files should end with a new line.
  - The first line of all files should be exactly `#!/usr/bin/python3`.
  - A `README.md` file at the root of the project folder is mandatory.
  - Code should follow the PEP 8 style guide (version 1.7.x).
  - All files must be executable.

## Task

### 0. UTF-8 Validation

- **Objective:** Write a method that determines if a given data set represents a valid UTF-8 encoding.
- **Prototype:** `def validUTF8(data)`
- **Return:** `True` if data is a valid UTF-8 encoding, else return `False`.
- **Notes:**
  - A character in UTF-8 can be 1 to 4 bytes long.
  - The dataset can contain multiple characters.
  - Data will be represented by a list of integers.
  - Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.

### Example Usage

```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False
```

## Repository

- **GitHub Repository:** [alx-interview](https://github.com/alx-interview)
- **Directory:** `0x04-utf8_validation`
- **File:** `0-validate_utf8.py`

## Conclusion

By studying the required concepts and utilizing the provided resources, you will be equipped to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data. Happy coding!
