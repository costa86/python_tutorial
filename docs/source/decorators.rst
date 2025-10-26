============
Decorators
============

This concept assumes you have already read the Functions chapter.
In Python, a decorator is an abstraction that allows you to use a function to extend the functionality of another function, without having to change it.

Let's see a very basic example:

.. code-block:: python
   :linenos:

    def print_start_and_end(func): 
        def wrapper():
            print("---START---")
            func()
            print("---END---")
        return wrapper

    @print_start_and_end
    def introduce():
        print("I am Michael")

    introduce()


.. code-block:: console
    
    ---START---
    I am Michael
    ---END---


Let's go over the implementation details:

``print_start_and_end(func)``

This is the decorator function. It takes another function as a parameter, then declares an inner placeholder function called "wrapper" (it could be any other name). 
Notice that ``wrapper`` is returned by ``print_start_and_end()`` , which triggers the call to ``print("---START---")``, then a call to ``func()`` function, 
then ﬁnally a call to ``print("---END---")``.

.. note::

    Notice that the ``func`` parameter references whatever function the decorator is used with. In our case, ``introduce()``.

``@print_start_and_end``

This is a syntax that signals the ``print_start_and_end()`` function is being used as a decorator. Notice the "@".

.. note::

    Notice it has to be placed in the line right above the ``introduce()`` decorated function, so that the decoration works as intended!

``introduce()``

Because this function is decorated (receives a decorator), whenever it's called, the ``print_start_and_end()`` decorator function will be triggered ﬁrst, 
which will then trigger the call to the ``introduce()`` within itself.

.. note::

    You may add multiple decorators to a single function. Just make sure they are all stacked right above the decorated function.

Decorating functions with parameters
--------------------------------

Parameters in the decorated function
--------------------------------

So far, neither the decorator nor the decorated function have taken any parameters. If you want to add them, a slight modiﬁcation is needed:

.. code-block:: python
   :linenos:

    def print_start_and_end(func):
        def wrapper(*args, **kwargs): # This is new 
            print("---START---")
            func(*args, **kwargs) # This is new too 
            print("---END---")
        return wrapper 

    @print_start_and_end
    def introduce(employee_name: str): 
        print(f"My name is {employee_name}")
    

.. note::

    Notice that I merely added ``*args`` and ``**kwargs`` to both ``wrapper()`` and the ``func()`` call inside ``print_start_and_end()``. 
    I could have added custom parameters instead (``employee_name``, in this case). But by using ``*args`` and ``**kwargs`` the decorator function 
    becomes more generic and therefore can accept any number of named or unnamed parameters.

Parameters in the decorator function
-----------------------------

Another possibility is to pass arguments to the decorator function itself, which can extend even more its capabilities. 
As a basic example, I will add a ``branch`` parameter. A few more tweaks are required, so take a closer look at the new wrapper functions inside 
the decorator, **specially their indentation levels**:

.. code-block:: python
   :linenos:

    def print_start_and_end(branch: str):
        def outer_wrapper(func): # This is new 
            def inner_wrapper(*args, **kwargs):
                print("---START---") 
                func(*args, **kwargs)
                print(f"I work at the {branch} branch") 
                print("---END---")

            return inner_wrapper 

        return outer_wrapper

    @print_start_and_end(branch="Scranton")
    def introduce(employee_name: str) -> None: 
        print(f"My name is {employee_name}")

    introduce("Jim")

Output:

.. code-block:: console

    ---START---
    My name is Jim
    I work at the Scranton branch
    ---END---
