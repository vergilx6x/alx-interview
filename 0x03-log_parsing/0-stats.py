#!/usr/bin/python3
'''A script for parsing HTTP request logs and computing metrics.
'''
import re


def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.

    Args:
        input_line (str): A single line from the HTTP request log.

    Returns:
        dict: A dictionary containing the status code and file size.
    '''
    pattern = (
        r'(?P<ip>\S+)\s*'  # IP address
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]\s*'  # Date and time
        r'"(?P<request>[^"]*)"\s*'  # HTTP request string
        r'(?P<status_code>\d+)\s*'  # Status code
        r'(?P<file_size>\d+)\s*'    # File size
    )

    match = re.fullmatch(pattern, input_line.strip())
    if match:
        return {
            'status_code': match.group('status_code'),
            'file_size': int(match.group('file_size'))
        }
    return {'status_code': '0', 'file_size': 0}


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.

    Args:
        total_file_size (int): The total file size.
        status_codes_stats (dict): A dictionary with
        counts of each status code.
    '''
    print(f'File size: {total_file_size}')
    for status_code, count in sorted(status_codes_stats.items()):
        if count > 0:
            print(f'{status_code}: {count}')


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.
        total_file_size (int): The current total file size.
        status_codes_stats (dict): The current count of status codes.

    Returns:
        int: The updated total file size.
    '''
    line_info = extract_input(line)
    status_code = line_info['status_code']
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    '''Starts the log parser and processes input line by line.'''
    total_file_size = 0
    status_codes_stats = {code: 0 for code in ['200', '301', '400', '401',
                                               '403', '404', '405', '500']}
    line_num = 0

    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats
                )
            line_num += 1

            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)

    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
