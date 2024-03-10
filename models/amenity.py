#!/usr/bin/python3
'''This is the state module
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''This is the amenity class inheriting from the BaseModel
    '''
    name: str = ""
