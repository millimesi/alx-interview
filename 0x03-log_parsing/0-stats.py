#!/usr/bin/python3
"""
Log parsing script that reads from stdin and computes metrics.
"""
import sys

# Initialize variables to store total file size and counts for each status code
total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_metrics():
    """
    Prints the computed metrics.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()

        # Validate the line format
        if len(parts) < 9:
            continue

        ip = parts[0]
        date = parts[3] + " " + parts[4]
        request = parts[5] + " " + parts[6] + " " + parts[7]
        status_code = parts[8]

        # Validate file_size presence and correctness
        try:
            file_size = int(parts[9])
            total_file_size += file_size
        except (IndexError, ValueError):
            continue

        # Update status code counts
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
    raise

print_metrics()
