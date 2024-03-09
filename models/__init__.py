#!/usr/bin/python3
'''
This is the __init__ module
'''
from models.engine.file_storage import FileStorage

storage = FileStorage()
''' creates a file storage instance '''

storage.reload()
''' calls reload to ensure updated info '''
