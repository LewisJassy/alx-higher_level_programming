#!/usr/bin/python3

import json

class Base:
    __nb_objects = 0
    def __init__(self, id = None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_objs):
        if list_objs is None or len(list_objs) == 0:
            return "[]"
        return json.dumps([obj.to_dictionary() for obj in list_objs])
        
    @staticmethod  
    def save_to_file(cls, list_objs):
        if list_objs == None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_objs))
