#!/usr/bin/python3

import sys


def print_my(d_sc, t_file_size):
    """
    printing method
    Args:
        d_sc: status code
        t_file_size: file size
    return:
        Nothing
    """

    print("File size: {}".format(t_file_size))
    for key, val in sorted(d_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


t_file_size = 0
code = 0
count = 0
d_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed = line.split()  # ✄ trimming
        parsed = parsed[::-1]  # inverting

        if len(parsed) > 2:
            count += 1

            if count <= 10:
                t_file_size += int(parsed[0])  # file size
                code = parsed[1]  # status code

                if (code in d_sc.keys()):
                    d_sc[code] += 1

            if (count == 10):
                print_my(d_sc, t_file_size)
                count = 0

finally:
    print_my(d_sc, t_file_size)
