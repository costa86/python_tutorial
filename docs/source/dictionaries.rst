============
Dictionaries
============

This is a way of creating mapping relationships in Python. Each element is composed of two parts: a key and a value. 
The syntax of a dict in Python is: ``{<key_1>: <value_1>, <key_2> : <value_2>, <key_n> : <value_n>}`` . See an example:

.. code-block:: python
   :linenos:

    employee = {
        "name": "michael scott",
        "position": "regional manager", 
        "age": 46,
        "past lovers": ["jan", "holly", "donna"], 
        "married": False
    }

    print(employee["past lovers"]) # => ["jan", "holly", "donna"] 
    print(employee["past lovers"][0]) # => jan 
    print(employee.get("name")) # => michael scott 
    print(employee.get("branch", "scranton")) # => scranton

    employee["gender"] = "male" # I can add new items 
    employee.update({"house owner": False}) # A new item can be added this way too

    print(employee.get("gender")) # => male
    print(employee.keys()) #=> dict_keys(['name', 'position', 'age', 'past lovers', 'married', 'gender', 'house owner'])
    print(employee.values()) #=> dict_values(['michael scott', 'regional manager', 46, ['jan', 'holly', 'donna'], False, 'male', False])


``employee["past lovers"]``

Note that this syntax is similar to the one used for getting elements by indexes in lists and tuples. But here, instead of an index, you use the "past lovers" key.

``employee["past lovers"][0]``

As you noticed, the value of ``employee["past lovers"]`` is a list containing three elements, so we can use the index to access a particular one.

``employee.get("name")``

This is an alternative way of accessing a value. It's the same as ``employee["name"]``. 

``employee.get("branch", "scranton")``

Do you see a key named "branch" in employee? No. This syntax is a way of setting a default value in case a given key is missing. 
So if a "branch" key was present and it had a value "x", then "x" would be returned instead of "scranton". This is a handy feature in a variety of situations.

``employee["gender"]``

Dictionaries are mutable, which means you can add this new key "gender" to it. You can change them too.

``employee.update({"house owner": False})``

This is an alternative way of adding new items.

Dict comprehension
------------------------

This concept assumes you have read the Loops, Deconstructing and Conditionals chapters.
This is an interesting feature in Python that allows you to create dicts out of collections, such as lists or tuples. 
By using a more concise and readable syntax:

.. code-block:: python
   :linenos:

    employees_list = [("angela", 50), ("michael", 46), ("pam", 30)]
    employees_dict = {k: v for k, v in employees_list} 
    employees_dict_over_30 = {k: v for k, v in employees_list if v > 30}

    print(employees_dict) # => {'angela': 50, 'michael': 46, 'pam': 30} 
    print(employees_dict_over_30) # => {'angela': 50, 'michael': 46}


``employees_dict``

This is a dict created with dict comprehension. Let's go over its details in two parts:

- Deﬁnes what will be in the new dict: ``k: v`` (``k`` for the key and ``v`` for the value)
- Deﬁnes the iteration over the original list: ``for k, v in employees_list`` (a tuple used as an iterator, where ``k`` is index 0 and ``v`` is index 1)

``employees_dict_over_30``

Also a dict created with dict comprehension. There's a third part now:

- Deﬁnes what will be in the new dict: ``k: v`` (same as the previous example) 	
- Deﬁnes the iteration over the original list: ``for k, v in employees_list`` (same as the previous example)
- Deﬁnes a conditional for ``k: v`` to be added to the dict: ``if v > 30`` (if the value of ``v`` is greater than 30)
