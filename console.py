#!/usr/bin/python3
"""
A simple command line interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """The console interpreter class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command that exits the program
        """
        return True

    def do_help(self, arg: str) -> bool | None:
        """Displays help information"""
        return super().do_help(arg)

    def do_EOF(self, arg):
        """Exits the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on emptyline by overiding default emtyline behaviour
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
