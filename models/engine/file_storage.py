#!/usr/bin/python3
# models/engine/file_storage.py
import json
from models.city import City
from models.state import State
from models.user import User
from models.review import Review


class FileStorage:
    #create a os filestorageengine
    
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
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for key, value in objs.items():
                    cls_name = value['__class__']
                    cls = globals().get(cls_name)
                    if cls:
                        self.__objects[key] = cls(**value)
                    else:
                        print(f"Warning: '{cls_name}' class not found.")
        except FileNotFoundError:
            pass  # This is normal if file doesn't exist yet
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
