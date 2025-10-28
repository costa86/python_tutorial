===========
Testing
===========

In real-words scenarios, your program is likely to change. Either to add new capabilities, 
refactor/change the already existent ones, or even to remove parts that are no longer needed.
With that growth in complexity, it may become cumbersome to make sure all the single parts of the program are working as intended. 

.. image:: https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExczZvdzh0ZHpuYWwyb3IycGwxMmhiNWZhOHM1eXo5NXBid3p6OHg1MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zfasHTHHvhtbRpdpZz/giphy.gif
   :alt: Description of the animation
   :align: center

---------------------------

This is a valid concern especially if you are working collaboratively, which is a context where someone may change something you created, or vice-versa.
For that reason, we are encouraged to implement tests to our programs. 
There are many approaches to creating tests in Python, with third-party libraries and also with the built-in unittest module, 
which is the one we will use in this chapter.

For the demonstration, we will have two ﬁles: 

*main.py*

.. code-block:: python
   :linenos:

    def get_alphabet_letters(qtd: int = 25, uppercase: bool = True) -> list[str]:

        if qtd <= 0 or qtd > 25:
            return []

        first = "A" if uppercase else "a"
        second = "B" if uppercase else "b"
        qtd -= 1

        return [chr(i) for i in range(ord(first), ord(second) + qtd)]



The ``get_alphabet_letters()`` function returns three diﬀerent possibilities:

1. An empty list. If ``qtd`` is less or equals to 0, or greater than 25.
2. A list with uppercase letters. If ``uppercase`` is ``True``.
3. A list with lowercase letters. If ``uppercase`` is ``False``.

*test_main.py*

.. code-block:: python
   :linenos:

    import unittest
    from main import get_alphabet_letters

    class TestGetAlphabetLetters(unittest.TestCase):

        def test_get_alphabet_letters_uppercase(self):
            expected = ["A", "B", "C"]
            result = get_alphabet_letters(3)
            self.assertEqual(expected, result)

        def test_get_alphabet_letters_lowercase(self):
            expected = ["a", "b", "c", "d"]
            result = get_alphabet_letters(4, False)
            self.assertEqual(expected, result)

        def test_get_alphabet_letters_zero(self):
            expected = []
            result = get_alphabet_letters(0)
            self.assertEqual(expected, result)

        def test_get_alphabet_letters_negative(self):
            expected = []
            result = get_alphabet_letters(-5)
            self.assertEqual(expected, result)

        def test_get_alphabet_letters_exceeds_length(self):
            expected = []
            result = get_alphabet_letters(26)
            self.assertEqual(expected, result)


    # The condition below is to ensure "unittest.main()" only runs if it's executed in this file itself, and not if it's imported by another file.
    if __name__ == "__main__":
        unittest.main()  # Run all the tests


Typically, these tests are made with asserts, which are veriﬁcations of whether a condition matches what you expected it to be. 
Let's go over some details about the implementation:

``TestGetAlphabetLetters``

The class' name is recommended to be descriptive about what we are going to test. Notice that it starts with "Test", 
which is a convention to express this as a test class. Also, notice that this class inherits from ``TestCase``, available in the ``unittest`` module.

``test_get_alphabet_letters_uppercase()``

Inside the class, we implement methods that will perform the actual tests. Notice the "test_" at the beginning of the method's name. 
Unlike the convention about the class' name we discussed above, this one is a **requirement** of ``unittest``!

``self.assertEqual(expected, result)``

Tests typically work by checking assertions. In our case, ``TestCase`` provides a range of methods to ﬁt your testing needs, 
such as this one for equality checks. Just to name a few others: ``assertLess()``, ``assertIsInstance()``, ``assertIsNone()`` and ``assertRaises()``. 
Check them all at https://docs.python.org/3/library/unittest.html#unittest.TestCase.	

``test_get_alphabet_letters_lowercase()`` and the other methods

Notice that all the methods are used to test only the ``get_alphabet_letters()`` function, although each one represents a different test case for it, 
as implied by their names. This is a recommended approach, as it helps visualize the cases that are not working if the tests fail, 
so we can ﬁx them and make all the tests pass, which is the desired state of any suite of tests.

In order to run the tests via command-line:

.. code-block:: console

    $ python3 -m unittest test_main.py

Output:

.. code-block:: console

    Ran 5 tests in 0.000s OK

.. note::

    These tests are what we call “unit tests”, which are meant to check if individual parts of the program are working as expected. 
    There are other types of tests, but they are out of the scope of this book:

    - **Integration tests**: are used to test the interaction between different components or modules of a software system. 
      They ensure that the components work together correctly and that data is passed between them correctly.
    - **System tests**: test the entire software system as a whole. 
      They are typically performed by a separate testing team and are used to validate that the system meets the requirements 
      specified in the system requirements specification.
    - **Acceptance tests**: these are used to validate that the software system meets the needs and expectations of the stakeholders, 
      such as the customers or end users. They are typically performed by the stakeholders and are used to ensure the software is accepted according to their criteria.
    - **Performance tests**: used to measure the performance of the software system under various conditions. 
      They are used to ensure that the system can handle the expected workload and that it meets the performance requirements specified in the system requirements specification.
    - **Security tests**: identify and mitigate security vulnerabilities in the software system. 
      They are used to ensure that the system is secure and that it meets the security requirements specified in the system requirements specification.
