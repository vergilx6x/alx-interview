#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics"""
import re
import sys


pattern = re.compile(
    r'^\d{1,3}(\.\d{1,3}){3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] '
    r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
)


line_count = 0
total_size = 0
status_codes = {code: 0 for code in ['200', '301', '400', '401',
                                     '403', '404', '405', '500']}


def print_stats():
    ''' Function to print current statistics '''
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


try:
    # Process log lines from stdin
    for log_line in sys.stdin:
        log_line = log_line.strip()
        match = pattern.match(log_line)

        if match:
            # Extract status code and file size
            status_code = match.group(2)
            file_size = int(match.group(3))

            # Update status code count and total file size
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += file_size

            line_count += 1

        # Every 10 lines, print the statistics
        if line_count == 9:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# Print remaining statistics if the input ends before hitting exactly 10 lines
if line_count > 0:
    print_stats()
