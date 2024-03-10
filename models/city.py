#!/usr/bin/python3
'''This is the city module
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''This is the city class inheriting from BaseModel
    '''
    state_id: str = ""
    name: str = ""
