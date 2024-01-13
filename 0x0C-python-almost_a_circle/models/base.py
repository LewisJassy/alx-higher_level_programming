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

    @classmethod
    def create(cls, **dictionary):
        """Method to create new instance directly from the class. Mainly
        for use by subclasses of Base.

        Args:
            dictionary (dict): Dictionary of attributes, value pairs
                with which to set attributes for new instance.

        Returns: New instance of class from which `create` was called.

        Raises: Errors delegated to subclasses of Base which call this
            method.
        """
        if cls.__name__ == "Rectangle":
            c = cls(1, 1)
        elif cls.__name__ == "Square":
            c = cls(1)
        else:
            c = cls()
        if not hasattr(dictionary, "keys") or not callable(dictionary.keys):
            dictionary = {}
        c.update(**dictionary)
        return c
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method to serialize list of dictionary objects into json.

        Args:
            list_dictionaries (list of dicts): List of dictionaries
                of attribute, value pairs for serialization into json
                representation.

        Returns: Json string representation of `list_dictionaries`.

        Raises: Any errors encounterd during serialization.
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Class method to convert `list_objs` to json string and
        save in file with name '<class name>.json'.

        Args:
            list_objs (list): list of objects of class from which
                this method is called.

        Raises: Any errors encountered during serialization and I/O.
        """
        if not list_objs:
            list_objs = []
        with open("{}.json".format(cls.__name__), 'w') as jf:
            jf.write(cls.to_json_string([obj.to_dictionary() for
                                         obj in list_objs]))
            
    def from_json_string(json_string):
        if json_string == None:
            return "[]"
        else:
            return json.loads(json_string)
        
    
