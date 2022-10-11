#!/usr/bin/python3

"""The console"""
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = '(hbnb)'

    def EOF(self, args):
        print("Quit command to exit the program\n")
        exit()

    def do_quit(self, args):
        print("Quit command to exit the program\n")
        exit()

    def help_EOF(self):
        print("Quit command to exit the program\n")

    def emptyline(self):
        pass

if  __name__ == '__main__':
    HBNBCommand().cmdloop()