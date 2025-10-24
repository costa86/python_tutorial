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

   ``name_2`` and ``name_3`: these are ways of representing multi-line


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
