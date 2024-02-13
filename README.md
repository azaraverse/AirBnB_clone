# AirBnB Clone Project
This repository contains the init AirBnB project that aims to create a clone of the AirBnb website as an educational exercise
in web development. The clone includes both a backend and a frontend, with backend being developed using [Python](https://www.python.org).

## Command Interpreter
The command interpreter is a part of the backend system that allows users to interact with the AirBnB clone through a command-line interface (CLI).
It provides a set of commands to manage various aspects of the application, such as creating and managing users, states, amenities, et cetera.

## Requirements
Python 3.8.5 or later

## How to start the Command Interpreter
1. Clone this repository onto your local system.
2. Navigate to the root of this repository.
3. Run the command `$ ./console.py` to start the command interpreter, in interactive mode.
    It should display this example screen format;
    ```bash
    azara@Ubuntu:~/AirBnB_clone$ ./console.py
    (hbnb) all MyModel
    ** class doesn\'t exist **
    (hbnb)
    (hbnb) show BaseModel
    ** instance id missing **
    (hbnb)
    (hbnb) show BaseModel My_First_Model
    ** no instance found **
    (hbnb)
    (hbnb) create BaseModel
    0f4d0985-d137-4e89-abb6-7e7a8604b9b2
    (hbnb)
    (hbnb) all BaseModel
    [\"[BaseModel] (0f4d0985-d137-4e89-abb6-7e7a8604b9b2) {\'id\': \'0f4d0985-d137-4e89-abb6-7e7a8604b9b2\', \'created_at\': datetime.datetime(2024, 2, 8, 16, 49, 7, 684312), \'updated_at\': datetime.datetime(2024, 2, 8, 16, 49, 7, 684328)}\"]
    (hbnb)
    (hbnb) show BaseModel 0f4d0985-d137-4e89-abb6-7e7a8604b9b2
    [BaseModel] (0f4d0985-d137-4e89-abb6-7e7a8604b9b2) {'id': '0f4d0985-d137-4e89-abb6-7e7a8604b9b2', 'created_at': datetime.datetime(2024, 2, 8, 16, 49, 7, 684312), 'updated_at': datetime.datetime(2024, 2, 8, 16, 49, 7, 684328)}
    (hbnb)
    (hbnb) destroy
    ** class name missing **
    (hbnb)
    (hbnb) update BaseModel 0f4d0985-d137-4e89-abb6-7e7a8604b9b2 first_name \"Azara\"
    (hbnb) show BaseModel 0f4d0985-d137-4e89-abb6-7e7a8604b9b2
    [BaseModel] (0f4d0985-d137-4e89-abb6-7e7a8604b9b2) {'id': '0f4d0985-d137-4e89-abb6-7e7a8604b9b2', 'created_at': datetime.datetime(2024, 2, 8, 16, 49, 7, 684312), 'updated_at': datetime.datetime(2024, 2, 8, 16, 50, 5, 779864), 'first_name': 'Azara'}
    (hbnb)
    (hbnb) create BaseModel
    3fa01046-9a52-4ca7-a041-7c1e0cd98228
    (hbnb)
    (hbnb) all BaseModel
    [\"[BaseModel] (0f4d0985-d137-4e89-abb6-7e7a8604b9b2) {\'id\': \'0f4d0985-d137-4e89-abb6-7e7a8604b9b2\', \'created_at\': datetime.datetime(2024, 2, 8, 16, 49, 7, 684312), \'updated_at\': datetime.datetime(2024, 2, 8, 16, 50, 5, 779864), \'first_name\': \'Azara\'}\", \"[BaseModel] (3fa01046-9a52-4ca7-a041-7c1e0cd98228) {\'id\': \'3fa01046-9a52-4ca7-a041-7c1e0cd98228\', \'created_at\': datetime.datetime(2024, 2, 8, 16, 50, 43, 634990), \'updated_at\': datetime.datetime(2024, 2, 8, 16, 50, 43, 635017)}\"]
    (hbnb)
    (hbnb) destroy BaseModel 0f4d0985-d137-4e89-abb6-7e7a8604b9b2
    (hbnb) show BaseModel 0f4d0985-d137-4e89-abb6-7e7a8604b9b2
    ** no instance found **
    (hbnb)
    (hbnb) quit

4. Run the command `$ echo "help" | ./console.py` to execute the help command in non-interactive mode.
    It should display this example screen format;
    ```bash
    $   echo \"help\" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF all create destroy help quit show update
    (hbnb)
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF all create destroy help quit show update
    (hbnb)
    $

For a complete list of commands and their usage, check `Documented commands` and use the `help` command.
