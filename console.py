# import cmd
# import json
# import models

# class HBNBCommand(cmd.Cmd):
#     prompt = '(hbnb) '

#     def do_quit(self, arg):
#         """Quit command to exit the program"""
#         return True

#     def do_EOF(self, arg):
#         """EOF command to exit the program"""
#         print()
#         return True

#     def emptyline(self):
#         """Do nothing on empty line"""
#         pass

#     def do_create(self, arg):
#         """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
#         if not arg:
#             print("** class name missing **")
#             return
#         try:
#             new_instance = eval(arg)()
#             new_instance.save()
#             print(new_instance.id)
#         except NameError:
#             print("** class doesn't exist **")

#     def do_show(self, arg):
#         """Prints the string representation of an instance based on the class name and id"""
#         if not arg:
#             print("** class name missing **")
#             return
#         args = arg.split()
#         if args[0] not in models.classes:
#             print("** class doesn't exist **")
#             return
#         if len(args) < 2:
#             print("** instance id missing **")
#             return
#         key = args[0] + '.' + args[1]
#         if key not in models.storage.all():
#             print("** no instance found **")
#             return
#         print(models.storage.all()[key])

#     def do_destroy(self, arg):
#         """Deletes an instance based on the class name and id (save the change into the JSON file)"""
#         if not arg:
#             print("** class name missing **")
#             return
#         args = arg.split()
#         if args[0] not in models.classes:
#             print("** class doesn't exist **")
#             return
#         if len(args) < 2:
#             print("** instance id missing **")
#             return
#         key = args[0] + '.' + args[1]
#         if key not in models.storage.all():
#             print("** no instance found **")
#             return
#         del models.storage.all()[key]
#         models.storage.save()

#     def do_all(self, arg):
#         """Prints all string representation of all instances based or not on the class name"""
#         args = arg.split()
#         if not arg:
#             print([str(v) for v in models.storage.all().values()])
#             return
#         if args[0] not in models.classes:
#             print("** class doesn't exist **")
#             return
#         print([str(v) for k, v in models.storage.all().items() if args[0] in k])

#     def do_update(self, arg):
#         """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
#         if not arg:
#             print("** class name missing **")
#             return
#         args = arg.split()
#         if args[0] not in models.classes:
#             print("** class doesn't exist **")
#             return
#         if len(args) < 2:
#             print("** instance id missing **")
#             return
#         key = args[0] + '.' + args[1]
#         if key not in models.storage.all():
#             print("** no instance found **")
#             return
#         if len(args) < 3:
#             print("** attribute name missing **")
#             return
#         if len(args) < 4:
#             print("** value missing **")
#             return
#         obj = models.storage.all()[key]
#         setattr(obj, args[2], type(getattr(obj, args[2]))(args[3]))
#         obj.save()

# if __name__ == '__main__':
#     HBNBCommand().cmdloop()
# import cmd
# import json
# import models

# class HBNBCommand(cmd.Cmd):
#     prompt = '(hbnb) '

#     def do_quit(self, arg):
#         """Quit command to exit the program"""
#         return True

#     def do_EOF(self, arg):
#         """EOF command to exit the program"""
#         return True

#     def emptyline(self):
#         """Called when an empty line is entered in response to the prompt"""
#         pass

#     def do_create(self, arg):
#         """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
#         args = arg.split()
#         if not arg:
#             print("** class name missing **")
#             return
#         if args[0] not in models.classes:
#             print("** class doesn't exist **")
#             return
#         obj = models.classes[args[0]]()
#         obj.save()
#         print(obj.id)

#     def do_show(self, arg):
#         """Prints the string representation of an instance based on the class name and id"""
#         args = arg.split()
#         if not arg:
#             print("** class name missing **")
#             return
#         if args[0] not in models.classes:
#             print("** class doesn't exist **")
#             return
#         if len(args) < 2:
#             print("** instance id missing **")
#             return
#         key = args[0] + '.' + args[1]
#         if key not in models.storage.all():
#             print("** no instance found **")
#             return
#         print(models.storage.all()[key])

#     def do_destroy(self, arg):
#         """Deletes an instance based on the class name and id (save the change into the JSON file)"""
#         args = arg.split()
#         if not arg:
#             print("** class name missing **")
#             return
#         if args[0] not in models.classes:
#             print("** class doesn't exist **")
#             return
#         if len(args) < 2:
#             print("** instance id missing **")
#             return
#         key = args[0] + '.' + args[1]
#         if key not in models.storage.all():
#             print("** no instance found **")
#             return
#         del models.storage.all()[key]
#         models.storage.save()



#     def do_update(self, arg):
#         """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
#         if not arg:
#             print("** class name missing **")
#             return
#         args = arg.split()
#         if args[0] not in models.classes:
#             print("** class doesn't exist **")
#             return
#         if len(args) < 2:
#             print("** instance id missing **")
#             return
#         key = args[0] + '.' + args[1]
#         if key not in models.storage.all():
#             print("** no instance found **")
#             return
#         if len(args) < 3:
#             print("** attribute name missing **")
#             return
#         if len(args) < 4:
#             print("** value missing **")
#             return
#         obj = models.storage.all()[key]
#         setattr(obj, args[2], type(getattr(obj, args[2]))(args[3]))
#         obj.save()

# if __name__ == '__main__':
#     HBNBCommand().cmdloop()

# def do_all(self, arg):
#     """Prints all string representation of all instances based or not on the class name"""
#     args = arg.split()
#     if not arg:
#         print([str(v) for v in models.storage.all().values()])
#         return
#     if args[0] not in models.classes:
#         print("** class doesn't exist **")
#         return
#     if hasattr(models, args[0]):
#         print([str(v) for v in getattr(models, args[0]).all()])
#     else:
#         print("** class doesn't exist **")

        

#     def do_update(self, arg):
#         """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
#         if not arg:
#             print("** class name missing **")
#             return
#         args = arg.split()
#         if args[0] not in models.classes:
#             print("** class doesn't exist **")
#             return
#         if len(args) < 2:
#             print("** instance id missing **")
#             return
#         key = args[0] + '.' + args[1]
#         if key not in models.storage.all():
#             print("** no instance found **")
#             return
#         if len(args) < 3:
#             print("** attribute name missing **")
#             return
#         if len(args) < 4:
#             print("** value missing **")
#             return
#         obj = models.storage.all()[key]
#         setattr(obj, args[2], type(getattr(obj, args[2]))(args[3]))
#         obj.save()

#     def do_all(self, arg):
#         """Prints all string representation of all instances based or not on the class name"""
#         args = arg.split()
#         if not arg:
#             print([str(v) for v in models.storage.all().values()])
#             return
#         if args[0] not in models.classes:
#             print("** class doesn't exist **")
#             return
#         if hasattr(models, args[0]):
#             print([str(v) for v in getattr(models, args[0]).all()])
#         else:
#             print("** class doesn't exist **")

#     def do_count(self, arg):
#         """Retrieves the number of instances of a class"""
#         args = arg.split()
#         if not arg:
#             print("** class name missing **")
#             return
#         if args[0] not in models.classes:
#             print("** class doesn't exist **")
#             return
#         count = 0
#         for obj in models.storage.all().values():
#             if obj.__class__.__name__ == args[0]:
#                 count += 1
#         print(count)

# if __name__ == '__main__':
#     HBNBCommand().cmdloop()
import cmd
import json
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in models.classes:
            print("** class doesn't exist **")
            return
        obj = models.classes[arg]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split('.')
        if len(args) != 2:
            print("** invalid format **")
            return
        class_name, obj_id = args[0], args[1]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        key = class_name + '.' + obj_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        if not arg:
            print([str(v) for v in models.storage.all().values()])
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        print([str(v) for k, v in models.storage.all().items() if args[0] in k])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = models.storage.all()[key]
        setattr(obj, args[2], type(getattr(obj, args[2]))(args[3]))
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
import cmd
import json
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        obj = models.classes[args[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        if not arg:
            print([str(v) for v in models.storage.all().values()])
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        print([str(v) for k, v in models.storage.all().items() if args[0] in k])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = models.storage.all()[key]
        setattr(obj, args[2], type(getattr(obj, args[2]))(args[3]))
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
