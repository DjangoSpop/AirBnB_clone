import json
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                class_name = key.split(".")[0]
                if class_name == "BaseModel":
                    obj = BaseModel(**value)
                elif class_name == "Place":
                    obj = Place(**value)
                elif class_name == "State":
                    obj = State(**value)
                elif class_name == "City":
                    obj = City(**value)
                elif class_name == "Amenity":
                    obj = Amenity(**value)
                elif class_name == "Review":
                    obj = Review(**value)
                else:
                    continue
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
