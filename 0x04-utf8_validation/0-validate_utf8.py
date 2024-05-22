#!/usr/bin/python3
"""
Module for UTF-8 Validation
"""


def validUTF8(data):
    """UTF-8 encoding"""
    n_bytes = 0

    for num in data:
        bin_rep = format(num, '#010b')[-8:]
        if n_bytes == 0:
            if bin_rep[0] == '0':
                continue
            elif bin_rep[:3] == '110':
                n_bytes = 1
            elif bin_rep[:4] == '1110':
                n_bytes = 2
            elif bin_rep[:5] == '11110':
                n_bytes = 3
            else:
                return False
        else:
            if bin_rep[:2] != '10':
                return False
            n_bytes -= 1

    return n_bytes == 0
