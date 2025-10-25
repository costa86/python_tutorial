============================
Operators
============================

Arithmetic operators	
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 10 30 30

   * - Operator
     - Description
     - Example
   * - `+`
     - Addition
     - ``3 + 5`` returns ``8``
   * - `-`
     - Subtraction
     - ``7 - 2`` returns ``5``
   * - `*`
     - Multiplication
     - ``2 * 4`` returns ``8``
   * - /
     - Division (float)
     - ``7 / 2`` returns ``3.5``
   * - //
     - Division (integer)
     - ``7 // 2`` returns ``3``
   * - %
     - Modulus (remainder)
     - ``7 % 2`` returns ``1``
   * - **
     - Exponentiation
     - ``2 ** 3`` returns ``8``

Assigning operators	
-----------------

.. list-table::
   :header-rows: 1
   :widths: 10 30 30

   * - Operator
     - Example
     - Equivalent to
   * - =
     - ``x = 5``
     - ``x = 5``
   * - +=
     - ``x += 3``
     - ``x = x + 3``
   * - -=
     - ``x -= 2``
     - ``x = x - 2``
   * - *=
     - ``x *= 4``
     - ``x = x * 4``
   * - /=
     - ``x /= 2``
     - ``x = x / 2``
   * - //=
     - ``x //= 3``
     - ``x = x // 3``
   * - %=
     - ``x %= 2``
     - ``x = x % 2``
   * - **=
     - ``x **= 3``
     - ``x = x ** 3``


Comparison operators
---------------------

.. list-table::
   :header-rows: 1
   :widths: 10 30 30 10

   * - Operator
     - Description
     - Example
     - Evaluates to
   * - ==
     - Equals to
     - ``5 == 5``
     - ``True``
   * - !=
     - Not equals to
     - ``5 != 5``
     - ``False``
   * - >
     - Greater than
     - ``5 > 3``
     - ``True``
   * - <
     - Less than
     - ``5 < 3``
     - ``False``
   * - >=
     - Greater than or equals to
     - ``5 >= 5``
     - ``True``
   * - <=
     - Less than or equals to
     - ``5 <= 3``
     - ``False``

Operator "is"
-----------------

This is a special comparison operator used to check whether the memory address is the same.

.. note::

    Checking for equality of memory addresses is not something you come across very often in Python programs, as it is a low-level concept. 
    But it's nice to know some basic details about it.

See next some examples to clarify the diﬀerences between the ``is`` and ``==`` operators:

.. code-block:: python
   :linenos:

    a = [1, 2]
    b = [1, 2]

    is_a_same_value_as_b = (a == b) # Do they have the same value? 
    is_a_same_memory_address_as_b = (a is b) # Do they point to the same memory address ?

    memory_address_of_a = id(a) 
    memory_address_of_b = id(b)

    print(is_a_same_value_as_b) # => True 
    print(is_a_same_memory_address_as_b) # => False 
    print(memory_address_of_a) # => 140712901292736 
    print(memory_address_of_b) # => 140712899331840

Logical operators
--------------------
.. list-table::
   :header-rows: 1
   :widths: 10 40 40

   * - Operator
     - Description
     - Example
   * - and
     - Returns ``True`` if all operands are ``True``
     - ``True and False`` returns ``False``
   * - or
     - Returns ``True`` if at least one operand is ``True``
     - ``True or False`` returns ``True``
   * - not
     - Returns ``True`` if the operand is ``False``
     - ``not True`` returns ``False``

More examples:

.. code-block:: python
   :linenos:

    # OPERATOR "AND":
    a = True and True # Both are True 
    print(a) # => True

    b = True and (1 == 2) and True # At least one is False 
    print(b) # => False

    c = ("jim" == "jim") and True and (5 > 1) # All are True 
    print(c) # => True

    d = False and False # At least one is False 
    print(d) # => False

    # OPERATOR "OR":
    e = True or False or False # At least one is True 
    print(e) # => True

    f = (1 == 1) or (2 == 2) # Parentheses are crucial here to remove ambiguity.
    # Also, at least one is True 
    print(f) # => True

    g = (1 > 2) or (2 == 1) or False # None of them are True 
    print(g) # => False

    h = False or False # None of them are True 
    print(h) # => False

Membership operators
-----------------
.. list-table::
   :header-rows: 1
   :widths: 10 40 40

   * - Operator
     - Description
     - Example
   * - in
     - Evaluates to True if a value is found in a collection
     - ``3 in [1, 2, 3, 4]`` returns ``True``
   * - not in
     - Evaluates to True if a value is not found in a collection
     - ``5 not in [1, 2, 3, 4]`` returns ``True``


These operators work with collections such as tuples, lists, sets and dicts:

.. code-block:: python
   :linenos:

    some_dict = {"name": "angela", "salary": 1000.0} 

    a = "name" in some_dict.keys()
    b = "name" in some_dict # Uses some_dict.keys() as default 
    c = "angela" in some_dict.values()
    d = "name" not in some_dict

    some_tuple = ("jim", "pam", "kevin") 
    e = "michael" not in some_tuple
    f = "jim" in some_tuple

    print(a) # => True 
    print(b) # => True 
    print(c) # => True 
    print(d) # => False 
    print(e) # => True 
    print(f) # => True


Operator precedence
---------------------------

This is an important concept, since it deﬁnes the order in which operations are performed. 
It works the same as in mathematical operations, where parentheses has higher precedence, meaning they are evaluated ﬁrst:

.. code-block:: python
   :linenos:
    
    a = (1 + 10) - (6 + 4) # Meaning (11) - (10)
    print(a) # => 1
    

Bitwise operators
--------------------

In Python, bitwise operators ( “|” , “&”,  “^”, “~”,  “<<”,  and “>>”) are mainly used for integer values and binary data. 
They can also be used for boolean values (``True`` and ``False``) which are internally represented as integers (1 and 0).
These operators are more used in the context of binary manipulation, which is a concept covered in the Bytes chapter. 
Read more about them at: https://wiki.python.org/moin/BitwiseOperators.	
Both "|" and "&" operators are used for concatenation and intersection, respectively. If you have read the Sets chapter, then you have already seen them.
