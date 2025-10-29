==================
Extra content
==================

This chapter explores some additional concepts to understand and others that can be implemented as supplements to your upcoming Python projects.

CLI - Command-Line Interface
---------------------------- 

As seen in the Loops chapter, you can have a Python program ask for a user’s input with the ``input()`` function. 
This kind of operation enables a wide range of possibilities for your programs, as you can have variables being dynamically set by the user, instead of hardcoding them.
Although in most real-life scenarios, these kinds of programs are often used in the context of task automation, 
where these arguments are passed in a slightly different way.

Try the following command:

.. code-block:: console

    $ python3 --help

You should see an output similar to this: 

.. code-block:: console

    Options (and corresponding environment variables):
    -b 	: issue warnings about str(bytes_instance), str(bytearray_instance)
            and comparing bytes/bytearray with str. (-bb: issue errors)
    -B 	: don't write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x
    -c cmd : program passed in as string (terminates option list)
    -d 	: turn on parser debugging output (for experts only, only works on
            debug builds); also PYTHONDEBUG=x
    […]

This output shows many parameters/options (also known as flags) that can be passed into Python. 
You have already used these flags when you created a virtual environment ( the ``-m`` flag, in this case).

This example shows how a CLI program is used to get arguments from the user, directly from the command-line.
Next, you will see how to create your own CLI programs in Python using different approaches:

Sys module
---------------

This built-in module is the most basic approach:

.. code-block:: python
   :linenos:

    import sys

    arguments = sys.argv

    help_message = """Arguments. In this order:
    name (string)
    age (int)"""

    if len(arguments) != 3:
        print(help_message)
        sys.exit()

    name, age = arguments[1:3]

    print(f"My name is {name}, and I am {age} yo")


Sample usage:

.. code-block:: console

    $ python3 main.py Jim 35

Output:

.. code-block:: console

    My name is Jim, and I am 35 yo


Let’s see how it works:

``arguments``

Try to ``print()`` this variable. It’s a list containing the file name itself (``main.py``), 
plus the extra arguments passed into the program: ``[“main.py”, “Jim”, 35]``.

``if len(arguments) != 3``

You may add multiple parameters to the CLI program, which get appended to the ``sys.argv`` list. 
I am only interested in the second and third parameters (index 1 and 2 in the list). So if any other number of parameters gets passed, 
I want the program to display a help message (similar to the ``--help`` flag on Python’s CLI), then exit (``sys.exit()``) the program itself.

Argparse module
--------------------------

This module allows you to create more complex CLI’s, as it provides options for validating types, setting flags to the parameters, and more. 
As expected, the official documentation is very detailed: https://docs.python.org/3/library/argparse.html. 
So I decided to create a more basic example:	

.. code-block:: python
   :linenos:

    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--branch",
        help="branch you work at",
        choices=["scranton", "stanford", "buffalo"],
    )
    parser.add_argument(
        "--name", help="your name", type=str, required=True, metavar="STRING"
    )

    parser.add_argument(
        "--sales", help="total in sales", type=float, default=0.0, metavar="FLOAT"
    )
    args = parser.parse_args()
    message = f"My name is {args.name}, I work at the {args.branch} branch. \
    My total in sales is {args.sales}"
    print(message)


In order to explain to the user how to use this program, the ``--help`` flag is available too. 
The same way you did to see all capabilities of Python’s CLI:

.. code-block:: console

    $ python3 main.py --help

Output:

.. code-block:: console

    usage: main.py [-h] [--branch {scranton,stanford,buffalo}] --name STRING [--sales FLOAT]

    options:
    -h, --help        	show this help message and exit
    --branch {scranton,stanford,buffalo}
                            branch you work at
    --name STRING     	your name
    --sales FLOAT     	total in sales

Third-party alternatives
---------------------------

In case the built-in argparse module doesn’t fit your needs, there are many third-party alternative libraries for creating professional CLI’s: 

- **Click** : https://click.palletsprojects.com/en/8.1.x/ (this is my go-to choice)
- **Typer**: https://typer.tiangolo.com/
- **Fire**: https://github.com/google/python-fire			
