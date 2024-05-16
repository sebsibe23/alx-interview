#!/usr/bin/python3
'''
A script for parsing HTTP request logs.
'''
import re


def extract_input(input_line):
    '''
    Extracts sections of a line of an HTTP request log.
    Parameters:
    input_line (str): The line from which to extract the information.
    Returns:
    dict: A dictionary containing the extracted information.
    The function uses regular expressions to extract the IP address,
    date, request, status code, and file size from the input line.
    If the input line matches the expected format, the function populates
    a dictionary with the extracted information and returns it.
    If the input line does not match the expected format, the function returns
    a dictionary with default values for status code and file size.
    '''
    try:
        log_fmt = '{}\\-{}{}{}{}\\s*'
        fpl = (
                r'\s*(?P<ip>\S+)\s*',
                r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
                r'\s*"(?P<request>[^"]*)"\s*',
                r'\s*(?P<status_code>\S+)',
                r'\s*(?P<file_size>\d+)'
                )
        info = {
                'status_code': 0,
                'file_size': 0,
                }
        log_fmt = log_fmt.format(fpl[0], fpl[1], fpl[2], fpl[3], fpl[4])
        resp_match = re.fullmatch(log_fmt, input_line)
        if resp_match is not None:
            status_code = resp_match.group('status_code')
            file_size = int(resp_match.group('file_size'))
            info['status_code'] = status_code
            info['file_size'] = file_size
        return info
    except Exception as e:
        print(e, flush=True)
        return None


def print_statistics(total_file_size, status_codes_stats):
    '''
       Prints the accumulated statistics of the HTTP request log.

    Args:
        total_file_size (int): The total file size accumulated
        from the HTTP request log.
        status_codes_stats (dict): A dictionary containing the
        frequency of each HTTP status code encountered in the log.

    Returns:
        None. The function prints the statistics to the console.

    Raises:
        None.

    Example:
        ```
        status_codes_stats = {'200': 10, '404': 5}
        print_statistics(1000, status_codes_stats)
        ```
    Output:
        ```
        File size: 1000
        200: 10
        404: 5
        ```
    '''
    try:
        print('File size: {:d}'.format(total_file_size), flush=True)
        for status_code in sorted(status_codes_stats.keys()):
            num = status_codes_stats.get(status_code, 0)
            if num > 0:
                print('{:s}: {:d}'.format(status_code, num), flush=True)
    except Exception as e:
        print(e, flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''
    Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which
        to retrieve the metrics.
        total_file_size (int): The total file size
        accumulated from the HTTP request log.
        status_codes_stats (dict):
        A dictionary containing
        the frequency of each HTTP status
        code encountered in the log.

    Returns:
        int: The new total file size.

    Updates the 'status_codes_stats' dictionary
    by incrementing the count of the HTTP status
    code found in the 'line' input.
    Also, it updates the 'total_file_size' by
    adding the 'file_size' from the 'line_info' dictionary.

    '''
    try:
        line_info = extract_input(line)
        status_code = line_info.get('status_code', '0')
        if status_code in status_codes_stats.keys():
            status_codes_stats[status_code] += 1
        return total_file_size + line_info['file_size']
    except Exception as e:
        print(e, flush=True)
        return total_file_size


def run():
    '''
    Starts the log parser.

    This function is the entry point for
    the log parser. It continuously
    reads input lines, updates the metrics,
    and prints statistics at regular
    intervals.

    Args:
        None

    Returns:
        None. The function runs indefinitely
        until interrupted.

    Raises:
        KeyboardInterrupt: If the user
        interrupts the program execution.
        EOFError: If the end of the input
        file is reached.

    Example:
        ```
        run()
        ```
    '''
    strline_num = 0
    tot_file_size = 0
    stat_codes_stats = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0,
            }
    try:
        while True:
            line = input()
            tot_file_size = update_metrics(
                    line,
                    tot_file_size,
                    stat_codes_stats,
                    )
            strline_num += 1
            if strline_num % 10 == 0:
                print_statistics(tot_file_size, stat_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(tot_file_size, stat_codes_stats)


if __name__ == '__main__':
    run()
