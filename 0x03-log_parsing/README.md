0x03. Log Parsing
Project Overview

This project focuses on parsing and processing log data streams in real-time using Python. we will build a script that reads log entries from standard input (stdin), extracts specific information, and calculates metrics based on the processed data.

Project Timeline:

Start Date: May 13, 2024, 6:00 AM
End Date (including Auto Review): May 17, 2024, 6:00 AM
Checker Release: May 14, 2024, 6:00 AM
Learning Objectives

Apply Python programming skills for data stream parsing and processing.
Handle data in a specific format (including error handling).
Perform calculations and derive metrics from log entries.
Concepts Covered

File I/O in Python (reading from stdin)
Signal Handling (handling CTRL+C interruption)
Data Processing (parsing, aggregation)
Regular Expressions (data validation)
Dictionaries (data organization)
Exception Handling
Resources

Python Input and Output (https://www.easypythondocs.com/input.html)
Python Signal Handling (https://docs.python.org/3/library/signal.html)
Python Regular Expressions (https://docs.python.org/3/library/re.html)
Python Dictionaries (https://docs.python.org/3/c-api/dict.html)
Python Exceptions (https://docs.python.org/3/library/exceptions.html)
Mock Technical Interview (provided by platform)
Requirements

General:
Allowed Editors: vi, vim, emacs
Execution Environment: Ubuntu 20.04 LTS, Python 3.4.3
Newline Character at End of Files
Shebang Line: #!/usr/bin/python3 at the beginning of all files
PEP 8 Style Guide (version 1.7.x) for code formatting
Executable Files
File Length Testing with wc
Task:
Develop a script (0-stats.py) that reads log entries from stdin line by line.
Expected Log Format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Process valid entries and calculate the following metrics:
Total File Size: Sum of all file sizes encountered.
Number of Lines by Status Code: Count occurrences of each unique status code (200, 301, 400, 401, 403, 404, 405, 500). Ignore invalid or non-integer status codes.
Print statistics every 10 lines or upon receiving a CTRL+C interruption.
Grading

The project will be evaluated based on functionality, code quality, and adherence to requirements. The provided checker script will automatically assess these aspects.

Additional Notes

Refer to the provided resources for a deeper understanding of the required concepts.
Feel free to utilize online resources and documentations beyond the provided ones.
Strive for clean, well-commented, and efficient code.
