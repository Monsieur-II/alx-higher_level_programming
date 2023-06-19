#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """"Prints dictionary by ordered keys"""
    keys = sorted(a_dictionary)
    for key in keys:
        print(f"{key}: {a_dictionary[key]}")
