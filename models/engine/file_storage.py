#!/usr/bin/python3
'''
This is the file storage module
'''
import json
import os


"""CLASSES = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "Place": Place,
        "Amenity": Amenity,
        "City": City,
        "Review": Review
        }
"""
    
class FileStorage:
    '''This is the file storage class
    '''
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def all(self):
        ''' returns a dictionary '''
        return (FileStorage.__objects)

    def new(self, obj):
        ''' sets the dictionary key value pair'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    """def save(self):
        ''' serializes objects to json file'''
        my_obj = {}
        for key, value in FileStorage.__objects.items():
            my_obj[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as jfile:
            json.dump(my_obj, jfile)

    def reload(self):
        '''deserializesbjson file to objects
        '''
        if os.path.exists(type(self).__file_path) is True:
            return
        try:
            with open(FileStorage.__file_path, 'r') as file:
                my_data = json.load(file)
                for key, value in my_data.items():

                    cls_name, obj_id = key.split('.')
                    cls = globals().get(cls_name)
                    if cls:
                        FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
        """
    def save(self):
        '''Serializes objects to json
        '''
        j_obj = {}
        for key, value in FileStorage.__objects.items():
            j_obj[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as j_file:
            json.dump(j_obj, j_file)

    def reload(self):
        '''Deserializes the json file back to dictionary
        '''
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as d_file:
                new_dict = json.load(d_file)
                new_dict = {kwesi: self.classes()[akua["__class__"]](**akua)
                for kwesi, akua in new_dict.items()}
                FileStorage.__objects = new_dict
        except FileNotFoundError:
            pass
