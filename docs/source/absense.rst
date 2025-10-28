============
Absense of a value
============
Many programming languages provide a way to represent the idea of lack or absence of a value. 
Many of them adopt the word “null" for that. But in Python, we use the ``None`` keyword:

.. image:: https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb3Z1cjA0MzNzeDd5YzBzdHhuM2dxZG5reXUxMXBwMWJtNGF6aWhwNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dTVWlxS6YXBRvcjT1E/giphy.gif
   :alt: Description of the animation
   :align: center
   
---------------------------

.. code-block:: python
   :linenos:

    print(None) # => None


``None`` can also be used as a conditional. See some examples:

.. code-block:: python
   :linenos:

    def get_name(name: str | None) -> str: 
        if not name:
            return "NAME IS ABSENT" 
        return name

    # A shorter alternative version
    def get_name_v2(name: str | None) -> str: 
        return name or "NAME IS ABSENT"

    print(get_name("michael")) # => michael 
    print(get_name(None)) # => NAME IS ABSENT 
    print(get_name_v2("jan")) # => jan 
    print(get_name_v2(None)) # => NAME IS ABSENT


In both previous functions, if the ``name`` argument is passed, then ``name`` itself is returned. But if ``None`` is passed, then "NAME IS ABSENT" is returned.

.. note::

    if you remember from the Functions chapter, ``None`` is implicitly returned in a function that apparently does not return anything. See this example:

    .. code-block:: python
        :linenos:

        def return_none():
            pass

        print(return_none()) => None

.. note::

    A fun fact about ``None`` is that it is a `Singleton <https://en.wikipedia.org/wiki/Singleton_pattern>`_ object in Python. You'll see more about objects in the Classes chapter.
