============
Strings
============


This is how you represent text in Python. Any of these syntaxes are valid strings:

.. code-block:: python
   :linenos:

   name_1 = "Stanley Hudson"
   name_2 = """
   Stanley
   Hudson
   """
   name_3 = """
   Stanley Hudson
   """
   name_4 = 'Stanley Hudson'


.. note::

   ``name_2`` and ``name_3`` are ways of representing multi-line


In more realistic scenarios, you are more likely to use strings composed by regular text plus other values obtained from variables. 
Let's say you want a string to greet someone based on their name:

.. note::

   This process is also known as “string/variable interpolation/substitution”. 

.. code-block:: python
   :linenos:

   name = "Angela"
   animal = "cat"
   greeting_1 = f"Welcome, {name}"
   greeting_2 = "Welcome, " + name
   greeting_3 = "Welcome, %s" % name
   greeting_4 = "Welcome, {}. Are you a {} person ?".format(name, animal)

   print(greeting_1)  # => "Welcome, Angela"
   print(greeting_2)  # => "Welcome, Angela"
   print(greeting_3)  # => "Welcome, Angela"
   print(greeting_4)  # => "Welcome, Angela. Are you a cat person ?"

Some explanation about these string variables:

``greeting_1``

This is the convention adopted throughout this book, since I ﬁnd it more convenient to use and readable. 
Also, it's the most modern approach. Notice the “f” must be placed right before the beginning of the string.

``greeting_2``
 
Notice the “+” sign. When dealing with strings, it means concatenation (joining). If you use it with numbers, such as integers or ﬂoats, it means a mathematical sum. 
This ability to perform different actions according to how it’s used is called polymorphism (poly=many, morph=form). 
So, in Python, the “+” sign is polymorphic. You will see about numbers in the Numbers chapter.

``greeting_3``

The “%s” stands for “string”. If the name variable was an integer, for instance, then “%i” should be used instead of “%s”.

``greeting_4``

The format method was used here (you’ll learn more about this in the Classes chapter), and the contents inside the curly brackets “{}” were replaced by the ``name`` and ``animal`` variables, respectively.


Replicating strings
------------

An interesting use case for strings is being able to replicate it multiple times by using the ``*`` operator, the same one used for multiplying numbers.

.. code-block:: python
   :linenos:
   branch = "Buffalo" 
   many_times = branch * 3
   print(many_times) # => "BuffaloBuffaloBuffalo"

Escape sequences
-----------------

These are special characters that can be used in strings to provide some additional features. They are denoted by a backslash ``\``, followed by the character. 
For instance:

.. list-table:: Special Character Reference
   :header-rows: 1
   :widths: 15 35

   * - Character
     - Meaning
   * - \\n
     - Newline character
   * - \\t
     - Tab character
   * - \\‘
     - Single quote
   * - \\“
     - Double quote
   * - \\b
     - Backspace character
   * - \\r
     - Carriage return character

.. code-block:: python
   :linenos:
   print("This is a\ttabbed string.")
   print("This is a\nstring with a new line.")
   print("This is a string with a backslash: \\")
   print('This is a string with a single quote: \'')
   print("This is a string with a double quote: \"")

.. code-block:: console
   This is a   	tabbed string.
   This is a
   string with a new line.
   This is a string with a backslash: \
   This is a string with a single quote: '
   This is a string with a double quote: "

Raw strings
------------------
In certain situations, you may want to actually use these escaped characters demonstrated above. 
A common use case is for ﬁle paths on Windows computers, which include the backslash "\" character. 
This can be accomplished by appending "r" right before the beginning of a string:

.. code-block:: python
   :linenos:
   jan_photo = r"C:\Users\Michael\princess_of_jamaica.jpg"
   print(jan_photo) # => C:\Users\Michael\princess_of_jamaica.jpg

Slicing strings
--------------------
You can get parts of a string by accessing their indexes. 
In Python, we start counting indexes/positions at 0, and negative indexes are counted backwards, from end to start. 
The concept of indexes and slicing will be covered in the Lists chapter.

.. code-block:: python
   :linenos:
   name = "RYAN"

   print(name[0]) # => R
   print(name[1]) # => Y
   print(name[2]) # => A
   print(name[3]) # => N
   print(name[-1]) # => N
   print(name[1:3]) # => YA

Some string methods
------------------------
Here are some usages of popular methods available for strings. 
Check them at https://docs.python.org/3/library/stdtypes.html#str.capitalize.  
The concept of "method" will be explained in the Classes chapter. 
For now, keep in mind they are a way of providing extra-capabilities to objects such as strings in this case. 
For example, turning a string into uppercase or lowercase. 
