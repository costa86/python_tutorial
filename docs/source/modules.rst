============
Modules
============

As your program grows, eventually it will become cluttered if it contains many lines. 
You will then realize that it makes more sense to split the program into multiple Python ﬁles (``.py``) and have them communicate with each other. 
This approach has many advantages, as it improves organization and reusability of functionalities in general.

In this case, I will still have ``main.py`` as a main entrypoint to the whole program. 
But I decided to store the information about the employees in a new folder ``/info``, where I placed two new ﬁles: ``sales.py`` and ``accounting.py``.

The resulted directory tree looks like this:

.. code-block:: rst

    ├── main.py
    └── info
        └── sales.py
        └── accounting.py


And the contents of the ﬁles:

``info/sales.py``

.. code-block:: python
   :linenos:

    employees_list = ["jim", "dwight", "andy", "stanley", "phyllis"]


``info/accounting.py``

.. code-block:: python
   :linenos:

    employees_list = ["oscar", "angela", "kevin"]


``main.py``

.. code-block:: python
   :linenos:

    # MODE 1
    from info.sales import employees_list 

    # MODE 2
    from info.sales import employees_list as el # Aliasing 

    # MODE 3
    from info.sales import * 

    # MODE 4
    import info.accounting

    print(employees_list) # => ['jim', 'dwight', 'andy', 'stanley', 'phyllis'] 
    print(el) # => ['jim', 'dwight', 'andy', 'stanley', 'phyllis'] 
    print(info.accounting.employees_list) #=> ["oscar", "angela", "kevin"]


We call "importing" the procedure of establishing a communication between two Python ﬁles. 
There are diﬀerent ways of performing an import. So let's go over them:

``MODE 1``

We are importing only the ``employees_list`` variable, which is located in the ``/info/sales.py`` ﬁle. 
With that, we can access this variable and call ``print()`` with it.

``MODE 2``

The same as ``MODE 1``. The only diﬀerence is that I am binding ``employees_list`` to a new variable ``el`` variable, so now the access 
to ``employees_list`` is made by referring to ``el`` instead. This is known as "aliasing" (creating an alias).

``MODE 3``

Here I am importing all the variables, classes and functions that are inside the ``/info/sales.py`` ﬁle, not just the ``employees_list`` variable.
Notice the "*" being used.

.. note::

    In programming, it's very common to see the asterisk character ("*") being used to represent the concept of "all" in certain contexts.

``MODE 4``

The ``/info/accounting.py`` ﬁle itself is being imported. In order to access its contents, we use dot notation (as seen in ``info.accounting.employees_list``).

The decision about which mode to adopt is very subjective and depends on the context and how the program is going to be used.
