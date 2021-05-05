#!/usr/bin/env python3
import os
import sys

sep = ","  # SEPARATOR FOR OUTPUT FILE . For tab use sep='"\t"'
schema = "input.csv"


def read_fields(file):
    """
    :param file: filepath
    :type file: str
    :return: list of fields specified in scheme
    :rtype: list
    """
    with open(file, 'r') as f:
        _fields_str = f.read()
    _fields_lst = _fields_str.strip().split(",")
    _fields_lst = [_str.strip() for _str in _fields_lst]
    return _fields_lst


def construct(filename, dest, _fields, sep):
    """
    This function constructs and returns valid tshark command
    :param filename: filename
    :type filename: str
    :param dest: output file
    :type dest: str
    :param _fields: extracted fields
    :type _fields: list
    :param sep: separator
    :type sep: str
    :return: tshark command
    :rtype: str
    """
    fields = "-e "+" -e ".join(_fields)
    cmd = 'tshark -r %s -T fields %s -E separator=%s -E occurrence=f > %s' % (filename, fields, sep, dest)
    return cmd


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Need to specify 2 commands\nExample python3 Converter.py xxx.pcap output.log")
    else:
        fields = read_fields(schema)
        filename = sys.argv[1]
        dest = sys.argv[2]
        cmd = construct(filename, dest, fields, sep)
        os.system(cmd)
