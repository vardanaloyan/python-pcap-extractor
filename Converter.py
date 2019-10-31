#!/usr/bin/env python3
import os, sys

sep = "," # SEPERATOR FOR OUTPUT FILE . For tab use sep='"\t"'
schema = "input.csv"

def readFields(file):
    urls_list = []
    with open(file, 'r') as f:
        _fields_str = f.read()
    _fields_lst = _fields_str.strip().split(",")
    _fields_lst = [_str.strip() for _str in _fields_lst]
    return _fields_lst

def Construct(filename, dest, _fields, sep):
    fields = "-e "+" -e ".join(_fields)
    cmd = 'tshark -r %s -T fields %s -E separator=%s -E occurrence=f > %s' % (filename, fields, sep, dest)
    return cmd

if len(sys.argv) != 3:
    print ("Need to specify 2 commands\nExample python3 Converter.py xxx.pcap output.log")
else:
    fields = readFields(schema)
    filename = sys.argv[1]
    dest = sys.argv[2]
    cmd = Construct(filename, dest, fields, sep)
    os.system(cmd)
