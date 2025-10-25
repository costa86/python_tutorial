============
Sets
============

This is another data type used to store values as a collection in Python. 
Sets oﬀer a very interesting feature, though: uniqueness of elements. This means that if you add the same element twice (or more) to a set, 
it will be ignored! This is useful if you want to ensure your collection does not contain any duplicated elements:


.. code-block:: python
   :linenos:

    group_1 = {"jim", "michael", "michael", "jan"} # Notice that "michael" was added twice

    group_1.add("pam") # This is how you can add new elements

    group_2 = set(["jim", "ryan", "kelly", "ryan"]) # It can be created this way too. Also, notice that "ryan" was added twice

    print(group_1) # => {'pam', 'jan', 'jim', 'michael'}
    print(group_2) # => {'ryan', 'kelly', 'jim'}


Notice that ``group_1`` and ``group_2`` don't contain any repeated elements, even though I tried to add duplicates into them.
Also, notice that when I ``print()`` them, the order of the elements is not respected! 
This has to do with some internal speciﬁcations on how Python stores these values in memory (it uses hash tables). 
As a consequence of that, you **cannot** access individual elements by index in a set, as we do in lists and tuples! 
As a workaround to this limitation, you can easily create a list out of a set:

.. code-block:: python
   :linenos:

    group_1 = list({"jim", "michael", "michael", "jan", "pam"}) # A list created out of a set. the second "michael" will be ignored
    print(group_1) # => ['jan', 'jim', 'pam', 'michael']

.. note::

    This procedure of converting a type into another (in this case, a tuple into a list), is known as “casting”.

Apart from this validation for uniqueness, another interesting use case for sets is performing union and intersection operations of elements in diﬀerent sets.

.. code-block:: python
   :linenos:

    group_1 = {"jim", "michael", "michael", "jan", "pam"}
    group_2 = {"jim", "ryan", "kelly", "ryan"}

    print(group_1.difference(group_2)) # => {'michael', 'pam', 'jen'} 
    print(group_1.union(group_2)) # => {'jim', 'pam', 'jen', 'ryan', 'kelly', 'michael'}

    easier_union = group_1 | group_2 # The same as the one above 

    print(easier_union) # => {'jim', 'pam', 'jen', 'ryan', 'kelly', 'michael'}
    print(group_1.intersection(group_2)) # => {'jim'} 

    easier_intersection = group_1 & group_2 # The same as the one above 

    print(easier_intersection) # => {'jim'}


.. note::

    If the symbols "|" and "&" are unfamiliar to you (as seen in ``easier_union`` and ``easier_intersection``), check out the bitwise operators in the Operators chapter.
