#!/usr/bin/python3
'''
This is the __init__ module
'''
from models.engine import file_storage

storage = file_storage.FileStorage()
''' creates a file storage instance '''

storage.reload()
''' calls reload to ensure updated info '''
