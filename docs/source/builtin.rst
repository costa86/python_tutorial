============
Some built-in functions
============

Built-in functions are already available to any Python program, so you don’t have to import them. 
Since we already covered some of them, such as ``enumerate()``, ``map()``, ``sum()`` and ``range()``, now it is a good time to talk about some others:

``any`` and ``all``
----------------
They are used to check whether any / all elements in a collection satisfy a given condition. They receive a collection and return a boolean.

.. code-block:: python
   :linenos:

    letters = ["a", "b", "c"]
    vowels = ["a", "e", "i", "o", "u"]

    is_there_any_vowel_in_letters = any([i for i in letters if i in vowels])
    conditions_to_check = [1 == 1, 3 > 2, "A" == "B"]
    are_all_elements_true = all(conditions_to_check)

    print(is_there_any_vowel_in_letters) #=> True
    print(are_all_elements_true) #=> False

As mentioned, ``any`` checks if any (at least 1) element in a collection is evaluated as ``True``, or ``False`` otherwise. 
On the other hand, ``all`` requires all elements (every single one) to be evaluated as ``True``, or ``False`` otherwise.

``is_there_any_vowel_in_letters``

The letter “a” (an element in ``letters``) exists in ``vowels``, so it returns ``True``.

``are_all_elements_true``

That one was close...almost all the elements in ``conditions_to_check`` are evaluated as ``True``, except the last one ``(“A” == “B”)``. As a result, it returns ``False``.

Sorted
------------

It receives a collection and returns it in sorted order (as a list). It also accepts a ``reverse`` (boolean) parameter, to sort it backwards. 
This is very handy to turn a collection of names into alphabetical order, for instance. 

.. note::

    If you recall from the Lists chapter, a list contains a ``.sort()`` method, which does pretty much the same thing as the ``sorted()`` function. 
    But this method does not exist on sets or tuples.

.. note::

    ``sorted()`` returns a list. Keep that in mind in case you are sorting a set or a tuple:

    .. code-block:: python
        :linenos:

        names_set = {"Jim", "Pam", "Angela"}
        numbers_tuple = (2, 1, 3)

        names_set_sorted = sorted(names_set)
        numbers_tuple_sorted_reverse = sorted(numbers_tuple, reverse=True)

        print(type(names_set_sorted)) #=> <class 'list'>
        print(names_set_sorted) #=> ['Angela', 'Jim', 'Pam']
        print(type(numbers_tuple_sorted_reverse)) #=> <class 'list'>
        print(numbers_tuple_sorted_reverse) #=> [3, 2, 1]
