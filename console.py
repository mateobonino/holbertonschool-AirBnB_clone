#!/usr/bin/python3
import cmd
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def EOF(self):
        exit()

    def do_quit(self):
        exit()

    def help_EOF(self):
        print("Quit command to exit the program\n")

    def help_quit(self):
        print("Quit commando to exit the program\n")

    def emptyline():
        pass

        if  __name__ == '__main__':
            HBNBCommand().cmdloop()