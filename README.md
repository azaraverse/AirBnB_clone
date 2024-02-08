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
    $   ./console.py
    (hbnb) create User
    abebd5c6-5abf-4cb9-80e6-bf38a74d6e72
    (hbnb) show User abebd5c6-5abf-4cb9-80e6-bf38a74d6e72
    [User] (abebd5c6-5abf-4cb9-80e6-bf38a74d6e72) {'id': 'abebd5c6-5abf-4cb9-80e6-bf38a74d6e72', 'created_at': datetime.datetime(2024, 2, 8, 6, 32, 50, 521901), 'updated_at': datetime.datetime(2024, 2, 8, 6, 32, 50, 521901)}
    (hbnb) update User abebd5c6-5abf-4cb9-80e6-bf38a74d6e72 name "Coder Azara"
    (hbnb) show User abebd5c6-5abf-4cb9-80e6-bf38a74d6e72
    [User] (abebd5c6-5abf-4cb9-80e6-bf38a74d6e72) {'id': 'abebd5c6-5abf-4cb9-80e6-bf38a74d6e72', 'created_at': datetime.datetime(2024, 2, 8, 6, 32, 50, 521901), 'updated_at': datetime.datetime(2024, 2, 8, 6, 32, 50, 521901), 'name': 'Coder Azara'}
    (hbnb) quit

4. Run the command `$ echo "help" | ./console.py` to execute the help command in non-interactive mode.
    It should display this example screen format;
    ```bash
    $   echo "help" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF help quit
    (hbnb)
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF help quit
    (hbnb)
    $

For a complete list of commands and their usage, use the 'help' command.
