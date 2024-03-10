#!/usr/bin/python3
'''This is the users module
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''The User class which inherits from the BaseModel
    '''

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
