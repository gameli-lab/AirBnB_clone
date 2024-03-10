#!/usr/bin/python3
'''This is the review module
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''This review class that inherits from the BaseModel
    '''
    place_id: str = ""
    user_id: str = ""
    text: str = ""
