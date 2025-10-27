============
Boolean
============

This is a data type used to represent a situation that can assume only one out of two possibilities. 
It's like the outcome of ﬂipping a coin: it must be either head or tails. There's no third option. 
Despite its simplicity, it's a very useful data type that can help remove ambiguity and provide clarity and elegance to your programs.

The two possible values for a boolean are ``True`` or ``False``.

.. image:: https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmpzcnNscGQ3YXUyeTU1Y28wcHBrZTQxYWttanpxd2R6M2lqdTNqYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dXFKDUolyLLi8gq6Cl/giphy.gif
   :alt: Description of the animation
   :align: center
   :loading: embed
                                                    
                                                                              
.. code-block:: python
   :linenos:

    # PART 1
    print(1 > 2) # => False 
    print(1 < 2) # => True 
    print(2 >= 2) # => True 
    print(6 > 6) # => False 
    print(5 == 5) # => True 
    tricky = 1 == 1 
    print(tricky) # => True

    # PART 2
    print("ryan" == "kelly") # => False 
    print("ryan" == "ryan") # => True 
    print("ryan" != "kelly") # => True 
    print(["pam"] == ["pam"]) # => True
    print(("michael", "jan") == ("michael", "holly")) # => False

    # PART 3
    def is_michael(name: str) -> bool: 
        return name == "michael"

    print(is_michael("michael")) # => True 
    print(is_michael("stanley")) # => False


``PART 1``

This is a basic mathematical comparison between numbers using the operators greater than (>), less than (<), and greater than or equals (>=).

``tricky``

This can cause confusion sometimes, because the operator for assigning values (=) is very similar to the operator for equivalence (==). 
Here, the value of this variable is equal to the output of the operation ``1 == 1`` (which is ``True``, since 1 is equal to 1). 
In this case, adding parentheses may improve readability. Feel free to write it as: ``tricky = (1 == 1)``. Read more about operators in the Operators chapter.

``PART 2``

The comparison works for strings and other data types as well. Notice that in ``print("ryan" != "kelly")`` 
I used the not equal operator (!=). In other words, it's like asking: is "ryan" diﬀerent than "kelly"? The answer is yes (``True``).

``PART 3``

This is a more realistic use case of a boolean. The ``is_michael()`` function returns the equality check between the ``name`` argument and the string "michael". 
Where it returns ``True`` if ``name`` is equals to (==) "michael". Otherwise, it returns ``False``. There is not a third possibility!

.. note::

    Notice I didn't need to explicitly write ``True`` or ``False`` as return options in ``is_michael()``. 
    This is the elegance and simplicity that I mentioned earlier about booleans.

.. note::

    A fun fact about ``True`` and ``False`` is that they are a `Singletons <https://en.wikipedia.org/wiki/Singleton_pattern>`_ objects in Python. You'll see more about objects in the Classes chapter.
