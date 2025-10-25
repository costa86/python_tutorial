============
Tuples
============

Similar to lists, a tuple is another way of creating a collection of values in Python. 
Apart from its syntax, the main diﬀerence between lists and tuples is that tuples are immutable, which means you cannot alter, 
add or remove elements in a tuple after it has been created!


.. code-block:: python
   :linenos:

    people_a = ("dwight", "darryl", "angela") 
    people_b = "dwight", "darryl", "angela"
    person_a = "dwight",
    person_b = ("dwight",)
    crazy_tuple = ("banana", 1, True, ["A", "B"], 50.0, {}) 

    print(people_a[1]) # => darryl


A few remarks:

``people_a`` and ``people_b``

Both are the same thing. The parentheses are optional when declaring tuples, although using them is the most used format. 
It's the comma-separation that actually creates a tuple!

``person_a`` and ``person_b``

Also both are the same. Notice the comma at the end, even if there's no second element. If no comma was present, it would be a string!

``crazy_tuple``

In a similar way to lists, a tuple can hold values of diﬀerent types.

Tuple comprehension
------------------------

This concept assumes you have read the Loops and the Conditionals chapters.
This is an interesting feature in Python that allows you to create tuples using a more concise and readable syntax:

.. code-block:: python
   :linenos:

    winners = ("dwight", "pam", "angela")

    winners_uppercase = tuple(i.upper() for i in winners)
    winners_containing_letter_a = tuple(i for i in winners if "a" in i)

    print(winners_uppercase) # => ('DWIGHT', 'PAM', 'ANGELA') 
    print(winners_containing_letter_a) # => ('pam', 'angela')


Explaining:

``winners_uppercase``

This is a tuple created with tuple comprehension. Let's go over its details in two parts:

- Deﬁnes what will be in the new tuple: ``i.upper()`` 	
- Deﬁnes the iteration over the original tuple: ``for i in winners`` 	

``winners_containing_letter_a``

Also a tuple created with tuple comprehension. There's a third part now:

- Deﬁnes what will be in the new tuple: ``i``
- Deﬁnes the iteration over the original tuple: ``for i in winners``
- Deﬁnes a conditional for i to be added to the new tuple: ``if "a" in i`` (if the letter "a" is found in ``i``)


Accessing indexes in tuples
-----------------------

The indexing rules and syntax for getting targeted elements and slices as seen in the Lists chapter are valid for tuples too:

.. code-block:: python
   :linenos:

    people = "jim", "pam", "dwight", "angela"

    print(people[2])  # => dwight
    print(people[-1])  # => angela
    print(people[:2])  # => ('jim','pam')


Tuples vs Lists
-----------------------

In case you are wondering when to use lists or tuples, since they are so similar, here's a few points for your consideration:

Tuples are a good choice when you want to ensure the elements are not accidentally modified. This is because tuples are immutable, meaning their elements cannot be changed once the tuple is created. 
If you have data that should remain constant, then using a tuple is a suitable option.

Tuples are optimized for performance in certain operations. They are faster for operations such as iterating over their elements or accessing them via index. 
If you need to access or iterate over the elements of a collection but don't need to modify it, using a tuple can be more suitable compared to a list.

Lists provide more flexibility compared to tuples. 
They allow you to change, add, or delete elements in a collection. 
If you anticipate needing to modify the elements of a collection or require more flexibility in general, then a list would be a more suitable choice.
