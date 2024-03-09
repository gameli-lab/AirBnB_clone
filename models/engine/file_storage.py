#!/usr/bin/python3
'''
This is the file storage module
'''
import json


class FileStorage:
    ''' This is the file storage class for the module. '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' returns a dictionary '''
        return (self.__objects)

    def new(self, obj):
        ''' sets the dictionary key value pair'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        ''' serializes objects to json file'''
        my_obj = {}
        for key, value in self.__objects.items():
            my_obj[key] = value.to_dict()

        with open(self.__file_path, 'w') as jfile:
            json.dump(my_obj, jfile)

    def reload(self):
        ''' deserializes json file to objects '''
        try:
            with open(self.__file_path, 'r') as file:
                my_data = json.load(file)
                for key, value in my_data.items():
                    cls_name, obj_id = key.split('.')
                    cls = globals().get(cls_name)
                    if cls:
                        self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
