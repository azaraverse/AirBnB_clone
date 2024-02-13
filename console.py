#!/usr/bin/python3
"""A simple command line interpreter that implements commands.

This module provides a command line interpreter class that allows users to
interact with a system through a command line interface. It implements
various commands for manipulating data stored in the system, such as
creating, updating, and deleting objects of different types.

Attributes:
    None

Classes:
    HBNBCommand: A command line interpreter class that implements various
    commands.

Functions:
    None
"""

import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """The console interpreter class."""

    intro = "Welcome to Azara's hbnb console!"
    prompt = '(hbnb) '
    methods = ['create', 'show', 'destroy', 'all', 'update']
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review,
    }

    def precmd(self, line: str) -> str:
        """Handles custom implementation of commands."""
        if not line or not line.endswith(')'):
            return line

        flag = 1
        for classs in self.__classes:
            for method in self.methods:
                if line.startswith(f'{classs}.{method}'):
                    flag = 0
        if flag:
            return line

        temp = ''
        for method in self.methods:
            temp = line.replace('(', '.').replace(')', '.').split('.')
            if temp[0] not in self.__classes:
                return ' '.join(temp)
            while temp[-1] == '':
                temp.pop()
            if len(temp) < 2:
                return line
            if len(temp) == 2:
                temp = f'{temp[1]} {temp[0]}'
            else:
                temp = f'{temp[1]} {temp[0]} {temp[2]}'

            if temp.startswith(method):
                return temp

        return ''

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file
        and prints the id.
        """
        args = parse(arg)
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f'{args[0]}()')
            new_instance.save()
            print(new_instance.id)

    @staticmethod
    def help_create():
        """static method that displays the help information of the
        create method.
        """
        print(
            'Usage: create <class_name> '
            '\nCreate would make an instance of a model and save this '
            'newly created instance to a JSON file.'
        )

    def do_show(self, arg):
        """Prints the string representation of an instance based on
        the class name and id.
        """
        args = parse(arg)
        if len(args) < 2:
            print('** instance id missing **')
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        key = f'{args[0]}.{args[1]}'
        if key not in storage.all():
            print('** no instance found **')
            return
        print(storage.all()[key])

    @staticmethod
    def help_show():
        """Static method that displays help information for
        the show command.
        """
        print(
            'Usage: show <class_name> <instance_id> '
            '\nShow the string representation of an instance '
            'based on the class name and instance ID.'
        )

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id,
        from memory.
        """
        args = parse(arg)
        if len(args) == 0:
            print('** class name missing **')
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        if args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        key = f'{args[0]}.{args[1]}'
        if key not in storage.all():
            print('** no instance found **')
            return
        del storage.all()[key]
        storage.save()

    @staticmethod
    def help_destroy():
        """Displays the help information of the destroy command."""
        print(
            'Usage: destroy <class_name> <instance_id> '
            '\nDeletes an instance based on the class name '
            'and instance ID.'
        )

    def do_all(self, arg):
        """Prints all string representations of all instances to stdout."""
        args = parse(arg)
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        else:
            class_name = args[0]
            if class_name not in self.__classes:
                print("** class doesn't exist **")
                return
            instances = storage.all().values()
            class_instances = [
                str(instance) for instance in instances
                if isinstance(instance, self.__classes[class_name])
            ]
            print(class_instances)

    @staticmethod
    def help_all():
        """Displays help information for all command."""
        print(
            'Usage: all -optional [<class_name>] '
            '\nPrints all string representations of instances '
            'based on the optional class name.'
        )

    def do_update(self, arg):
        """This updates an instance based on the class name and id."""
        args = parse(arg)
        if len(args) == 1:
            print('** instance id missing **')
            return
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 0:
            print('** class name missing **')
            return
        else:
            key = f'{args[0]}.{args[1]}'.strip(',')
            print(storage.all().keys())
            instance = storage.all()[key]
            if key not in storage.all():
                print('** no instance found **')
                return
            # print('Instance retrieved:', storage.all().get(key))
            if len(args) == 2:
                print('** attribute name missing **')
                return
            elif len(args) == 3:
                print('** value missing **')
                return
            else:
                try:
                    attribute_type = type(getattr(instance, args[2]))
                    args[3] = attribute_type(args[3])
                except AttributeError:
                    pass
                try:
                    eval(args[3])
                except (SyntaxError, NameError):
                    args[3] = f"'{args[3]}'"
                print(args[2])
                setattr(instance, args[2].strip('," '), eval(args[3]))
                instance.save()

    @staticmethod
    def help_update():
        """Displays help information for the update command."""
        print(
            'Usage: update <class_name> <instance_id> <attribute_name> '
            '"<attribute_value>" '
            '\nUpdates an instance based on the class name, instance ID, '
            'attribute name, and attribute value.'
        )

    def do_quit(self, arg):
        """Quit command that exits the program
        """
        return True

    def do_EOF(self, arg):
        """Exits the program on Ctrl+D"""
        print()
        return True

    def emptyline(self):
        """Do nothing on emptyline by overiding default emtyline behaviour
        """
        pass


def parse(line):
    """Handles command line parsing using shell logic"""
    return shlex.split(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
