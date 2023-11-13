#!/usr/bin/python3
"""
console.py module: Contains the entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class: The command interpreter class which inherits from cmd.Cmd.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def default(self, line):
        """Default action when no match is found"""
        pass

    @staticmethod
    def _print_objects():
        """Prints all objects in memory."""
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(f"{arg}()".format(arg))
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")
        except Exception as e:
            print(f"Error: {e}")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = f"{args[0]}.{args[1]}"

        if args[0] in BaseModel.__subclasses__().__name__ and key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        obj_dict = storage.all()
        key = f"{args[0]}.{args[1]}"

        if args[0] in BaseModel.__subclasses__().__name__ and key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

            return

        obj_dict = storage.all()
        key = f"{args[0]}.{args[1]}"

        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

   
    def do_all(self, arg):
        subclasses = [cls.__name__ for cls in BaseModel.__subclasses__()]
        if arg in subclasses:
            print([str(obj) for obj in storage.all().values() if type(obj).__name__ == arg])
        elif not arg:
            print([str(obj) for obj in storage.all().values()])
        else:
            print("** class doesn't exist **")
    def complete_create(self, text, line, begidx, endidx):
        """Completes the create command."""
        return [cls.__name__ for cls in BaseModel.__subclasses__()]
    
    def do_update(self, arg):
        args = self.parse_update_args(arg)
        if not args:
            return

        class_name, instance_id, attribute_name, attribute_value = args
        obj_dict = storage.all()
        obj_key = f"{class_name}.{instance_id}"

        if obj_key not in obj_dict:
            print("** no instance found **")
            return

        obj = obj_dict[obj_key]
        try:
            # Attempt to set the attribute with the correct type
            self.set_object_attribute(obj, attribute_name, attribute_value)
        except AttributeError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Invalid value for attribute: {e}")
        else:
            obj.save()

    def parse_update_args(self, arg):
        """Parses the arguments for the update command and returns them or prints an error."""
        args = arg.split()
        if len(args) < 4:
            error_messages = [
                "** class name missing **",
                "** instance id missing **",
                "** attribute name missing **",
                "** value missing **"
            ]
            print(error_messages[len(args)])
            return None
        return args[:4]  # Return the first four arguments

    def set_object_attribute(self, obj, attribute_name, attribute_value):
        """Sets an attribute of an object, attempting to use the correct type."""
        attribute_value = attribute_value.strip("\"'")
        if hasattr(obj, attribute_name):
            attr_type = type(getattr(obj, attribute_name))
            attribute_value = attr_type(attribute_value)
        setattr(obj, attribute_name, attribute_value)
    def print_instances_of_class(self, class_name):
        obj_dict = storage.all()
        for obj in obj_dict.values():
            if obj.__class__.__name__ == class_name:
                print(obj)
    def print_all_instances(self):
        obj_dict = storage.all()
        for obj in obj_dict.values():
            print(obj)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
