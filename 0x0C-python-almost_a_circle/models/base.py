#!/usr/bin/python3
"""Defines a Base Class"""
import json
import csv


class Base:
    """
    A parent class from which other classes
    will be created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initiates a new instance
        Args:
            id : the id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON representation of a list of dictionaries
        Args:
            list_dictionaries: the list of dicts
        """
        if list_dictionaries is None or not len(list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves json representation of objects to a file
        list_objs: the list of objects
        """
        new = []
        if list_objs is not None:
            for i in list_objs:
                new.append(i.to_dictionary())

        new = cls.to_json_string(new)
        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            file.write(new)
            file.close()

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of a json string representation
        :param json_string: the string
        """
        if json_string is None or not len(json_string):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance with all attributes set
        :param dictionary: dict containing attributes
        :return: The instance created
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                text = file.read()
                list_t = cls.from_json_string(text)
                new = []
                for i in list_t:
                    new.append(cls.create(**i))
                return new
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes to a file in csv format"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w") as file:
            if list_objs is None or not len(list_objs):
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["width", "height", "x", "y", "id"]
                elif cls.__name__ == "Square":
                    fieldnames = ["size", "x", "y", "id"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for dic in list_objs:
                writer.writerow(dic.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="w") as file:
                if filename == "Rectangle.csv":
                    fieldnames = ["width", "height", "x", "y", "id"]
                elif filename == "Square.csv":
                    fieldnames = ["size", "x", "y", "id"]

                dic_list = csv.DictReader(file, fieldnames=fieldnames)
                dic_list = [dict([key, int(value)] for key, value in d.items()) for d in dic_list]
                return [cls.create(**d) for d in dic_list]
        except IOError:
            return []
