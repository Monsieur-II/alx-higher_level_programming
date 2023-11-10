#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not len(list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        dics = []
        if list_objs is not None:
            for i in list_objs:
                dics.append(i.to_dictionary())

        dics = cls.to_json_string(dics)
        if not list_objs:
            filename = "Base.json"
        else:
            filename = list_objs[0].__class__.__name__ + ".json"

        with open(filename, "w") as file:
            file.write(dics)
            file.close()
