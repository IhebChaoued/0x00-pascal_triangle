#!/usr/bin/python3
"""Log Parsing"""

import sys
import signal
import re


total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_statistics():
    print("File size:", total_file_size)
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))

def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    line_count += 1
    line = line.strip()

    match = re.match(r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)$', line)
    if match:
        ip_address, date, status_code, file_size = match.groups()
        status_code = int(status_code)
        file_size = int(file_size)

        total_file_size += file_size

        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

    if line_count % 10 == 0:
        print_statistics()
