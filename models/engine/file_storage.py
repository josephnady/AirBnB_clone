#!/usr/bin/python3
import json


class FileStorage:
    """class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances"""
    __objects: dict = {}
    __file_path: str = 'file.json'

    def all(self, cls=None):
        """returns the dictionary __objects"""
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in type(self).__objects.items():
                if cls == value.__class__ or \
                        cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        stored_items_ids = \
            [keys.split('.')[1] for keys in self.all().keys()]
        if obj.id in stored_items_ids:
            return
        key = obj.__class__.__name__ + '.' + obj.id
        type(self).__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        How it works:
        <class 'BaseModel'> -> to_dict() ->
        <class 'dict'> ->  FJSON dump ->  <class 'str'> -> FILE"""
        json_objects = {}
        for key in type(self).__objects:
            # very important code as it leads to read all the obj in json
            json_objects[key] = type(self).__objects[key].to_dict()
        with open(type(self).__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file does not exist,
        no exception should be raised)
        How It Works:
        <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>"""
        from models import classes
        try:
            with open(type(self).__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    type(self).__objects[key] = \
                        classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete instance from JSON file and save changes"""
        if obj is not None:
            try:
                del self.all()[obj]
                self.save()
            except Exception:
                raise "Wrong obj format, Usage <ClassName>.<ClassID>"

    def update(self, key, kwargs):
        """Update Object based on key and kwargs"""
        self.all()[key].__dict__.update(**kwargs)
        self.save()
