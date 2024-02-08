#!/usr/bin/python3
"""
Serializing instances to a JSON file and
Deserializing JSON file to instances
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """A storage class that serialises instances to a JSON file
    and deserialises a JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}
    def all(self):
        return self.__objects

    def new(self, obj):
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        serialised_objs = {}
        for key, value in self.__objects.items():
            serialised_objs[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as json_file:
            json.dump(serialised_objs, json_file)

    def reload(self):
        try:
            with open(
                self.__file_path, 'r', encoding='UTF-8'
                ) as json_file:
                loaded_objs = json.load(json_file)
                for key, value in loaded_objs.items():
                    cls = value['__class__']
                    self.new(eval('{}({})'.format(cls, '**value')))
        except FileNotFoundError:
            pass
