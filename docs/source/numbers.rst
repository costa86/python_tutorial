============
Numbers
============

In Python, numbers can be represented as three diﬀerent types:

.. image:: https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3JjdWdjODcxdzNhYTZnY3RmNTNqeGdicHlkZGV6Y3NmNG85Zm1lZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SEWEmCymjv8XDbsb8I/giphy.gif
   :alt: Description of the animation
   :align: center

Int
-----------

Short for "integer". This type is used to represent whole numbers. Being positive, negative, or zero.

.. code-block:: python
   :linenos:

    a = 5
    b = 123456789101112
    c = -45
    d = 0

    # Use type(<some_variable>) to return the type of a variable:

    print(type(a)) # => <class 'int'>
    print(type(b)) # => <class 'int'>
    print(type(c)) # => <class 'int'>
    print(type(d)) # => <class 'int'>


Float
----------------

Also can be positive, negative or zero. It's used to represent decimal numbers. Floats can also be used to represent 
`scientiﬁc notation <https://en.wikipedia.org/wiki/Scientific_notation>`_, adopting "e" to indicate the power of 10.

.. code-block:: python
   :linenos:

    a = 1.50
    b = 0.0
    c = -48.68
    d = 4e3 # scientific notation, equals to 4000.0 
    e = 4e-3 # scientific notation, equals to 0.004

    print(type(a)) # => <class 'float'> 
    print(type(b)) # => <class 'float'> 
    print(type(c)) # => <class 'float'> 
    print(type(d)) # => <class 'float'> 
    print(type(e)) # => <class 'float'>

Complex
-----------

A "complex" is a number with a real and an imaginary part, where the imaginary part is a multiple of the imaginary unit "j".


.. code-block:: python
   :linenos:
    
    a = 3 + 5j 
    b = 5j
    c = -5j

    print(type(a)) # => <class 'complex'> 
    print(type(b)) # => <class 'complex'> 
    print(type(c)) # => <class 'complex'>

