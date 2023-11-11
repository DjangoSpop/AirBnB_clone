#!/usr/bin/python3
# models/engine/file_storage.py
import json
from models.city import City
from models.state import State
from models.user import User
from models.review import Review


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
                for key, value in objs.items():
                    cls_name = value['__class__']
                    cls = globals()[cls_name]
                    FileStorage.__objects[key] = cls(**value)
        except FileNotFoundError:
            return