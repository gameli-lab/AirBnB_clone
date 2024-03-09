#!/usr/bin/python3
""" This is the my module for the base model class. """
from models import storage

from datetime import datetime
from uuid import uuid4


class BaseModel():
    '''Initialisation of the base model'''
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
            if 'id' not in kwargs:
                storage.new(self)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        cls_name = self.__class__.__name
        '''Custom string rep of the base model instance'''
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        ''' Updates the time'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ''' returns a dictionary'''
        obj_dict = self.__dict__
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return (obj_dict)
