============
Match statement
============

Formally known in Python as Structural Pattern Matching, the match case statement is another structure to handle multiple conditionals, 
yet providing more ﬁne-grained control over the possibilities, and reducing the cluttering that may come from complex conditionals 
created using the traditional ``if-elif-else``.

.. code-block:: python
   :linenos:
    
    def get_employees_by_department(department: str) -> list:

        match department.lower():

            case "sales":
                return ["jim", "dwight", "phyllis", "stanley"]

            case "accounting":
                return ["angela", "oscar", "kevin"]

            case "human resources" | "human_resources":  # either one
                return ["toby"]

            case "reception":
                return ["pam"]

            case _: # no match
                return []


    print(get_employees_by_department("human_resources"))  # => ['toby']
    print(get_employees_by_department("accounting"))  # => ['angela', 'oscar', 'kevin']
    print(get_employees_by_department("management"))  # => []


In this example, the two new keywords to pay attention to are ``match`` and ``case``. Following, let’s understand the control ﬂow in a match case.

The ``get_employees_by_department()`` function returns a list of employees' names based on their department, represented by the ``department`` 
parameter that it receives. Notice the last case "_", which is roughly equivalent to the ``else`` part in an ``if-elif-else`` statement. 
In this case, I decided to return an empty list. 

.. note::

    The usage of  "_" is covered in the Deconstructing chapter.
