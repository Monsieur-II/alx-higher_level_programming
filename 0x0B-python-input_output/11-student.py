#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """Inits an object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of object"""
        if isinstance(attrs, list) and all(type(x) == str for x in attrs):
            return {y: getattr(self, y) for y in attrs if hasattr(self, y)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of object"""
        for x, y in json.items():
            setattr(self, x, y)
