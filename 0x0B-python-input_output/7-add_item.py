#!/usr/bin/python3
"""Script that adds all arguments to a python list"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    dest = "add_item.json"
    try:
        my_list = load_from_json_file(dest)
    except Exception:
        my_list = []

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, dest)
