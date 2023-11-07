#!/usr/bin/python3
"""
console.py module: Contains the entry point of the command interpreter.
"""

import cmd
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

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file, and prints the id."""
        if not arg:
            print("** class name missing **")
            return

        try:
            obj = eval(f"{arg}()")
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

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

        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        obj_dict = storage.all()
        if arg:
            if arg in BaseModel.__subclasses__().__name__:
                print([str(obj) for key, obj in obj_dict.items() if type(obj).__name__ == arg])
            else:
                print("** class doesn't exist **")
        else:
            print([str(obj) for obj in obj_dict.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **" if len(args) == 0 else "** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        obj_dict = storage.all()
        key = f"{args[0]}.{args[1]}"

        if key in obj_dict:
            obj = obj_dict[key]
            try:
                attr_type = type(getattr(obj, args[2]))
                value = attr_type(args[3].strip("\"'"))
                setattr(obj, args[2], value)
                obj.save()
            except AttributeError:
                setattr(obj, args[2], args[3].strip("\"'"))
                obj.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
