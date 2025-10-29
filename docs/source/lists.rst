============
Lists
============

This is one of the most typical ways in Python to store collections of values.

.. image:: https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGhtOHdydzlxZHVuZzUxdXZpZ2ZzM2s5NjRlOHJ6bzE1ZXl4MjVxbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/x1CTRDahCslouG0RpW/giphy.gif
   :alt: Description of the animation
   :align: center
   
---------------------------

.. code-block:: python
   :linenos:

    winners = [
        "jim",
        "dwight",
        "oscar",
        "darryl",
        "andy",
        "toby",
        "phyllis",
        "angela",
        "kevin",
    ]

    crazy_list = ["banana", 1, True, ["A", "B"], 50.0, {}]
    

.. note::

    As seen in ``crazy_list``, a list may hold values of diﬀerent types.

Accessing elements in a list
-------------------------

A crucial concept to grasp in order to work with lists is "indexes". Each element in a list is automatically assigned a number, starting at 0, according to their position.

So, in the ``winners`` list:

+---------+-------+---------------+
| Element | Index | Negative index|
+=========+=======+===============+
| jim  | 0     | -9            |
+---------+-------+---------------+
| dwight  | 1     | -8            |
+---------+-------+---------------+
| oscar  | 2     | -7            |
+---------+-------+---------------+
| darryl   | 3     | -6            |
+---------+-------+---------------+
| andy    | 4     | -5            |
+---------+-------+---------------+
| toby    | 5     | -4            |
+---------+-------+---------------+
| phyllis   | 6     | -3            |
+---------+-------+---------------+
| angela   | 7     | -2            |
+---------+-------+---------------+
| kevin   | 8     | -1            |
+---------+-------+---------------+

With that in mind, you can access individual elements by referring to their indexes:

.. code-block:: python
   :linenos:

    print(winners[0])  # => jim
    print(winners[1:4])  # => ['dwight', 'oscar', 'darryl']
    print(winners[-1])  # => kevin
    print(winners[:3])  # => ['jim', 'dwight', 'oscar']
    print(winners[4:])  # => ['andy', 'toby', 'phyllis', 'angela', 'kevin']


A few notes:

``winners[1:4]``

Note that the syntax for slicing a list is ``<list>[<ﬁst index> : <last index>]``. The ﬁrst index is inclusive, and the last index is exclusive. 
What it means in practice is that "1:4" actually ranges the elements starting at index 1 and ﬁnishing at index 3 (4-1). This characteristic is inherited from the mathematical concept of intervals. 
In this case, the first index 1 is a closed (inclusive) interval, and the second index 4 is an open (exclusive) interval. 
See below a visual representation of this idea:

.. code-block:: rst

     1	          4
    [x]----------[ ]


``winners[-1]``

By using a negative number, the index number is counted backwards, where -1 means the last element in the list. 
So, in this case "oscar" can be accessed by both indexes 6 and -1, "toby" by 5 and -2, and so on.

.. note::

    Being able to select the negative index is very convenient. Let's say you have a huge list and you wish to access its last element. 
    Instead of visually checking its position, you can simply select the index -1.

``winners[:3]``

Omitting the ﬁrst index is a shortcut for the ﬁrst index (0), so this is the same as 0:3. 

``winners[4:]``

Omitting the last index is a shortcut for the last index (-1), so this is the same as 4:-1.

Validation if a list has elements
------------------------------------

This concept assumes you have read both Functions and Conditionals chapters.
Consider the following situation: you have a function that receives a list. 
If the list has elements, the function performs action "A", but if the list is empty, then it performs action "B".
You may use the ``len()`` function to get the number of elements in a list.

.. code-block:: python
   :linenos:

    winners = ["dwight", "pam", "angela", "kevin", "phyllis", "toby", "oscar"]
    losers = []

    print(len(winners)) # => 7
    print(len(losers)) # => 0


.. note::

    The ``len()`` function can be used for other types too, such as dicts and strings.

It's very common for people to assume you need to check whether the quantity of elements in the list is greater than 0 ( ``len(winners) > 0`` ) to accomplish that. 
But in Python there's a convenient abstraction for checking whether a list has elements or is empty:

.. code-block:: python
   :linenos:

    winners = ["dwight", "pam", "angela", "kevin", "phyllis", "toby", "oscar"] 
    losers = []

    def handle_list(some_list: list) -> None: 
        if some_list:
            print("list has values") 
        else:
            print("list is empty")


    handle_list(winners) # => list has values 
    handle_list(losers) # => list is empty



List comprehension
----------------

This concept assumes you have read the Loops chapter.
This is an interesting feature in Python that allows you to create lists using a more concise and readable syntax:

.. code-block:: python
   :linenos:

    winners = ["dwight", "pam", "angela", "kevin", "phyllis", "toby", "oscar"]

    # You may also use a tuple as a source:
    # winners = ("dwight", "pam", "angela", "kevin", "phyllis", "toby", "oscar")

    winners_uppercase = [i.upper() for i in winners]
    winners_containing_letter_a = [i for i in winners if "a" in i]

    print(winners_uppercase) #=> ['DWIGHT', 'PAM', 'ANGELA', 'KEVIN', 'PHYLLIS', 'TOBY', 'OSCAR']

    print(winners_containing_letter_a) #=> ['pam', 'angela', 'oscar']

    # Another interesting example is creating a list of numbers:
    numbers_from_1_to_5 = [i for i in range(1, 6)]

    print(numbers_from_1_to_5) # => [1, 2, 3, 4, 5]

    # And creating a list with the alphabet letters:

    alphabet_letters = [chr(i) for i in range(ord("A"), ord("B") + 25)]

    print(alphabet_letters) #=> ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


Explaining:

``winners_uppercase``

This is a list created with list comprehension. Let's go over its details in two parts:

- Deﬁnes what will be in the new list: ``i.upper()``
- Deﬁnes the iteration over the original list: ``for i in winners`` 

``winners_containing_letter_a``

Also a list created with list comprehension. There's a third part now:

- Deﬁnes what will be in the new list: ``i``
- Deﬁnes the iteration over the original list: ``for i in winners``	
- Deﬁnes a conditional for ``i`` to be added to the new list: ``if "a" in i`` (if the letter "a" is found in ``i``)


Some methods in lists
--------------------------

There are many built-in methods to extend the capabilities of a list. Visit: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists to see them all.  
Next, a few of the most popular ones:

.. code-block:: python
   :linenos:

    winners = ["dwight", "pam", "angela", "kevin", "phyllis", "toby", "oscar"]

    winners.pop(1) # The element at index 1 ("pam") was removed from the list

    winners.append("jim") # Now "jim" is included in the list

    winners.sort() # Now the list is in alphabetical order

    print(winners) # => ['angela', 'dwight', 'jim', 'kevin', 'oscar', 'phyllis', 'toby']
