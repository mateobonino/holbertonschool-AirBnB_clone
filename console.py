#!/usr/bin/python3
"""The console"""
import cmd
import json
from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = '(hbnb) '
    ClassList = ["Amenity", "BaseModel", "City", "Place", "Review", "State", "User"]

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, arg):
        """Create new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            if arg in self.ClassList:
                new = eval(arg)()
                new.save()
                print("{}".format(new.id))
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        The string representation of an instance based on the class name
        """
        var = arg.split(" ")
        if len(var) == 1 and var[0] == "":
            print("** class name missing **")
        else:
            if var[0] not in self.ClassList:
                print("** class doesn't exist **")
            elif len(var) == 1:
                print("** instance id missing **")
            else:
                my_dict = storage.all()
                for obj in my_dict:
                    var2 = obj.split(".")
                    if var2[1] == var[1]:
                        print("{}".format(my_dict[obj]))
                        return
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name"""
        var = arg.split(" ")
        if len(var) == 1 and var[0] == "":
            print("** class name missing **")
            return
        if len(var) < 2:
            print("** instance id missing **")
            return
        if var[0] not in self.ClassList:
            print("** class doesn't exist **")
            return
        try:
            my_dict = storage.all()
            key = var[0] + '.' + var[1]
            my_dict[key]
        except:
            print("** no instance found **")
            return
        with open('file.json', 'w') as f:
            del my_dict[key]
            f.write(json.dumps(my_dict, default=str))
            storage.reload()

    def do_all(self, arg):
        """Prints all string representation based or not on the class name"""
        lis = []
        var = arg.split(" ")
        my_dict = storage.all()
        if len(var) == 1 or var[0] == "":
            for i in my_dict:
                lis.append(str(my_dict[i]))
            print(lis)
            return
        if var[0] not in self.ClassList:
            print("** class doesn't exist **")
            return
        for obj in my_dict:
            var2 = obj.split(".")
            if var2[1] == var[1]:
                lis.append(str(my_dict[obj]))
            print(lis)

    def do_update(self,arg):
        """Updates an instance based on the class name"""
        var = arg.split(" ")
        if len(var) == 1:
            print("** class name missing **")
        else:
            if var[0] not in self.ClassList:
                print("** class doesn't exist **")
            elif len(var) == 1:
                print("** instance id missing **")
            else:
                my_dict = storage.all()
                for obj in my_dict:
                    var2 = obj.split(" ")
                    if var2[1] == var[1]:
                        print("{}".format(my_dict[obj]))
                        return
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
