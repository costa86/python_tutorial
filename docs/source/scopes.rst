==================
Scopes
==================

This chapter assumes you have read the Functions chapter.
This is a concept used in many programming languages. It's basically an area/boundary in which variables are reachable in a program. 
The body (inside area) of a function, for instance, is the function’s scope.

.. warning::

    Keep in mind that handling these scopes in Python is not a trivial task. If not done properly, a range of unexpected behaviors may occur. So use it wisely!

Global
------------------

As the name implies, it's the broader scope. It's reachable in the whole program:

.. code-block:: python
   :linenos:

    age = 4

    def change_age_globally(): 
        global age
        age = 10

    print(f"Initial value of 'age': {age}") #=> Initial value of 'age': 4 
    change_age_globally()
    print(f"Final value of 'age': {age}") #=> Final value of 'age': 10


Nonlocal
-----------------

This one requires 2+ nested functions. As an example, consider two functions “A” and “B”, where “B” is nested (inside) in “A”. 
The ``nonlocal`` scope of “B” is the same as the local scope of “A”.

Let’s see a practical example to make it clear:


.. code-block:: python
   :linenos:

    age = 4


    def change_age_outer():
        # N1
        age = 10

        def change_age_inner():
            # N2
            nonlocal age
            age = 50

        print(f"2. Initial value of 'age' in the local scope of 'change_age_outer()':{age}")

        # N3
        change_age_inner()

        print(f"3. Final value of 'age' in local scope of 'change_age_outer()':{age}")


    print(f"1. Initial value of 'age' in global scope: {age}")
    change_age_outer()  # N4
    print(f"4. Final value of 'age' in global scope: {age}")



This time I decided to label the comment notes as “N’s”.  See their explanations:
 
**N1:** This area is the local scope of ``change_age_outer()``, and also he ``nonlocal`` scope of ``change_age_inner()``.
**N2:** Here is the local scope of ``change_age_inner()``
**N3:** This call will change ``age`` in the local scope of ``change_age_outer()``, because of the ``nonlocal`` keyword.
**N4:** This will not affect the value of ``age`` in the global scope

Output:

.. code-block:: console

    1. Initial value of 'age' in global scope: 4
    2. Initial value of 'age' in the local scope of 'change_age_outer()':10
    3. Final value of 'age' in local scope of 'change_age_outer()':50
    4. Final value of 'age' in global scope: 4


``globals`` and ``locals`` (built-ins)
------------------

These are two very important built-in functions in Python.
See this:

.. code-block:: python
   :linenos:

    print(globals())

Output:

.. code-block:: console

    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f1911bfd880>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/myuser/projects/python_course/main.py', '__cached__': None}


The return of ``globals()`` is a dictionary containing all the values available in the global scope of the current program.  
You might find it interesting to know that all these values are available as variables too. Try ``print(__name__)``, and you’ll get “__main__”, and so on.

Feel free to run some experiments: create new variables and functions, import variables from other files, then ``print(globals())`` again to see how it changes!

Now, let’s see about the ``locals()`` function.


.. code-block:: python
   :linenos:

    def test(age: int):
        print("LOCAL START")
        print(locals())
        print("LOCAL END")

    name = "Michael"
    test(46)
    print(globals())


Output:

.. code-block:: console

    LOCAL START
    {'age': 46}
    LOCAL END
    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f518a3017c0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/costa/projects/python_course/main.py', '__cached__': None, 'test': <function test at 0x7f518b7f22a0>, 'name': 'Michael'}


In short, ``locals()`` works very similarly to ``globals()``, but in its own self-contained scope, which, in this situation, was the body of the ``test()`` function. 
When I called ``test()`` with 46, ``{“age”: 46}`` became part of the scope of the function, and was added to its ``locals()``, which, as you can see, is a dict as well.

Also, take a look at the two last items of ``globals()``. The test function and the name variable were added there.
As you can see, both these functions can be very handy in situations where you need to inspect what is actually “visible” by your current program.
