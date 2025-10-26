============
Error/exception handling
============

In programming, sometimes things don't happen as we expect, and problems may occur. 
In Python, we call these problems "exceptions". Exceptions have diﬀerent types, so it's easier to understand their meaning. 
For instance, write and try to run this program:


.. code-block:: python
   :linenos:

    print(1 / 0)


Instead of seeing the result, you will get some weird message similar to this one:

.. code-block:: console

    Traceback (most recent call last):
    File "/home/myuser/coding/python_book/main.py", line 1, in <module> print(1 / 0)
    ~~^~~
    ZeroDivisionError: division by zero


Well, you cannot divide 1 by 0. That's a problem... As a result, Python decides to stop the execution of the program and leaves a message to you, 
so you can understand and ﬁx the problem. In this case it was an exception of type ``ZeroDivisionError``.

Now try this one:

.. code-block:: python
   :linenos:

    employees = ["ryan", "pam", "creed"] 
    print(employees[3])


Output:

.. code-block:: console

    Traceback (most recent call last):
    File "/home/myuser/coding/misc/python_book/main.py", line 2, in <module> print(employees[3])
    ~~~~~~~~~^^^
    IndexError: list index out of range


Notice that the ``employees`` has only three elements, so their valid indexes are only 0, 1 and 2. Since Python cannot reach index 3, the program crashes. 
But now the exception has a diﬀerent type: ``IndexError``.

Visit this website to see all the built-in Python exception types: https://docs.python.org/3/library/exceptions.html. 

In many cases, having the whole program crash whenever an exception happens is not very convenient… 
That's why Python provides features for handling exceptions, so that the program can "recover" itself and keep its execution ﬂow, instead of crashing. 
Let's see this in action:

.. code-block:: python
   :linenos:

    employees = ["ryan", "pam", "creed"] 
    index = 3

    try:
        print(employees[index])

    except IndexError as e:
        print(f"Index {index} is not valid: {e}") 

    finally:
        print("I get printed regardless of the index being valid or not")


Output:

.. code-block:: console

    Index 3 is not valid: list index out of range
    I get printed regardless of the index being valid or not


Let's go over the implementation details:

``try``

As the name implies, this keyword signals the program will attempt (try) to do something that may or may not work, such as accessing an index in a list. 
In other words, I am aware that there's a possibility of an exception to take place here.
But if instead of 3, you use 0, 1 or 2 as ``index``, then ``print(employees[index])`` works as expected and the program continues its execution ﬂow, 
since these are valid indexes.

``except IndexError as e``

A new keyword here: ``except``. This is where the exception handling takes place. 
Here I am saying that if an exception of type ``IndexError`` happens (which is the case here, since index is set to 3), 
then the program will ``print()`` a message: "Index 3 is not valid: list index out of range". But it continues to work instead of crashing!
A very important detail here is that I am being explicit about the exception type I want to handle: ``IndexError``. 
If any other type of exception happens instead, the program crashes... A "safer" alternative would be using the ``Exception`` type instead of ``IndexError``. 
This is because ``Exception`` is a parent class of ``IndexError``, so another error type would certainly be caught as well.

.. note::

    In certain situations, you may want to handle diﬀerent exception types in speciﬁc ways, so that's the reason Python provides this ﬂexibility of either targeting a speciﬁc exception type, or using a more generic one such as Exception. Also note that the reference to the exception inside the printed string is made via this e variable. By stating "except IndexError as e", I am setting a variable called "e" as an alias to IndexError. The concept of aliasing is explained in the Modules chapter.

``ﬁnally``

This part is optional. The block of code delimited by the ``ﬁnally`` keyword gets executed if both cases: whether the ``try`` block works or an exception happens. 
It's like saying: "regardless of what happens, run this piece of code".

Pass
---------------

Another keyword you can use in an except block is ``pass``. Let’s say you don’t want to handle a particular exception yet, so you can just write ``pass``, 
instead of doing something. Basically, ``pass`` works as a placeholder with no effect. 

.. code-block:: python
   :linenos:

    def test():
        try:
            1 / 0
        except ZeroDivisionError:
            pass
        print("test")

    test() # => test

.. warning::

    Keep in mind that using ``pass`` instead of letting an exception be raised is typically not advisable in real projects, 
    as you are potentially preventing the program from raising and exception when it was supposed to! It's like you're suppresing some expected behavior of the program.
    This is commonly known as “silent fail”, and it might hide critical issues that need to be handled properly. So use it wisely! 

Another use case for ``pass`` is when you create a function, but don’t want to create its functionality yet, so you simply write ``pass`` within its body. 
Think of it as a “to-do” label, so-to-speak. Example:

.. code-block:: python
   :linenos:

    def do_nothing_yet():
        """
        I will implement this function later
        """
        pass


Raising exceptions
---------------------

You may also want to deliberately cause an exception, or “raise” it, as it’s known. The ``raise`` keyword is used for that:

.. code-block:: python
   :linenos:

    def introduce_accountant(name: str) -> str:
        accountants = ["oscar", "angela", "kevin"]
        
        if name not in accountants:
            raise ValueError(f"{name} is not an accountant")
        
        return f"{name} is an accountant"

    print(introduce_accountant("oscar")) #=> oscar is an accountant
    print(introduce_accountant("michael")) # will raise an exception…


If ``introduce_accountant()`` gets called with a ``name`` not included in ``accountants``, then an exception of type ``ValueError`` is raised. 
That’s what happened when I called it with “michael”. Here’s the output:

.. code-block:: console

    Traceback (most recent call last):
    File "/home/myuser/python_book/main.py", line 10, in <module>
        print(introduce_accountant("michael"))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/home/myuser/python_book/main.py", line 4, in introduce_accountant
        raise ValueError(f"{name} is not an accountant")
    ValueError: michael is not an accountant

