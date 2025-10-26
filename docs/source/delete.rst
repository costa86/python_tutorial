============
Deleting objects
============

In Python, ``del`` is a keyword used to delete an object or a variable from the memory, so it’s no longer accessible by the program. 
Here are some examples of how it can be used:


.. code-block:: python
   :linenos:

    # 1. Deleting variables:
    employee_name = "pam" 

    del employee_name

    print(employee_name) # Raises a NameError exception: "name 'employee_name' is not defined"

    # 2. Deleting some elements in a collection, such as a list: 
    winners = ["dwight", "pam", "angela"]

    del winners[0]

    print(winners) #=> ['pam', 'angela']

    # 3. Deleting keys in a dict:
    employee = {"name": "michael", "age": 46} 

    del employee["age"]

    print(employee) #=> {'name': 'michael'}
