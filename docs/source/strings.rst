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

=======  ======  ======
Header1  Header2 Header3
=======  ======  ======
A        B       C
D        E       F
=======  ======  ======

.. list-table:: Example Table
   :widths: 25 25 50
   :header-rows: 1

   * - Name
     - Age
     - Occupation
   * - Alice
     - 30
     - Developer
   * - Bob
     - 28
     - Writer
