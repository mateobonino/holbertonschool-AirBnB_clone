#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    def EOF():
        quit()

        if  __name__ == '__main__':
            HBNBCommand().cmdloop()