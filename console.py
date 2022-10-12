#!/usr/bin/python3
"""The console"""
import cmd
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

    def do_create(self, arg):
        if not arg:
            print("** class name mission **")
        else:
            if arg in self.ClassList:
                print("{}".format(arg.id))
            else:
                print("** class doesn't exist **")

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("")
        return True

    def help(self):
        print("Quit command to exit the program\n")
    
    def emptyline(self):
        pass

if  __name__ == '__main__':
    HBNBCommand().cmdloop()