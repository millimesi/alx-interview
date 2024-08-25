#!/usr/bin/python3
"""
Log parsing
"""
import sys

# Initialize
all_size = 0
status_amount = {
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
    print(f"File size: {all_size}")
    for c in sorted(status_amount.keys()):
        if status_amount[c] > 0:
            print(f"{c}: {status_amount[c]}")


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
        status_c = parts[8]

        # Validate file_size presence and correctness
        try:
            file_size = int(parts[9])
            all_size += file_size
        except (IndexError, ValueError):
            continue

        # Update status c counts
        if status_c in status_amount:
            status_amount[status_c] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
    raise

print_metrics()
