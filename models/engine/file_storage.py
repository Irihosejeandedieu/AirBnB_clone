#!/usr/bin/python3
"""This is the class to store files"""

import json
from base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """This class is for the abstracted objects 
    Attributes:
        _file_path(str): The name of file to save our object.
        _objects(dicts): This is the dictionary for instantiated objects.
    """
    _file_path = "file.json"
    _objects = {}

    def all(self):
        """returns the dictionary of the __object.."""
        return FileStorage.__objects
    def new(self, obj):
        """set the key <obj_class_name> to the object"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """serilize the file __file_path to json fofrmat"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w")as f:
            json.dump(objdict, f)
    
    def reload(self):
        """deserialize the __file_path file to __objects, if it exists.."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
 