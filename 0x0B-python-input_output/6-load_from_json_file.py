#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Creates an object from a json file"""
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
