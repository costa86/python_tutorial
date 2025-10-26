============================
Functions
============================

This is a process of extracting values from data structures such as lists, tuples, and dicts, and assigning them to isolated variables in a single statement. 
This is also known as "unpacking".

.. code-block:: python
   :linenos:

    name, position = ("oscar", "accountant") 
    print(name) # => oscar
    print(position) # => accountant

    # In dicts we use the values (method ".values()") below
    branch_name, active = {"name": "scranton", "is_active": True}.values() 

    print(branch_name) # => scranton
    print(active) # => True

A few remarks:

Notice that the order matters here. The variables will match their respective position in the collection.
When deconstructing a dict, the variable's names do not need to match the keys' names. Only the position matters. 
See that I deconstructed ``branch_name`` to the "name" key and ``active`` to the "is_active" key.

Another interesting use case is to use deconstructed values as function arguments.


.. code-block:: python
   :linenos:

    employee_list = ["oscar", "meredith", "pam"]

    def print_names(*names): 
        for i in names:
            print(i)

    print_names("oscar", "meredith", "pam") 
    print_names(*employee_list)


The output of both calls to ``print_names()`` is the same:

.. code-block:: console

    oscar 
    meredith 
    pam


And another example using a dict as a `**kwargs` argument:

.. code-block:: python
   :linenos:

    def print_employee_info(name: str, age: int, gender: str): 
        print("Name:", name)
        print("Age:", age) 
        print("Gender:", gender)

    employee = {"gender": "male", "age": 37, "name": "Dwight"} 
    print_employee_info(**employee)


Output:

.. code-block:: console

    Name: Dwight 
    Age: 37 
    Gender: male

Notice that in the previous example, the order of the keys in the employee dict doesn't match the respective deconstructed variables described 
as parameters in the ``print_employee_info()`` function. So, based on the rules I mentioned earlier, it should not work. But it does work!
The reason it works is because ``employee`` was passed to the function as a `**kwargs` argument. 
If you recall from the Functions chapter, there's a very distinct diﬀerence in calling a function with unnamed arguments (*args) and named arguments (**kwargs). 
As a result, what matters here is that the keys in ``employee`` have an exact match to the parameters' names in the ``print_employee_info()`` function.

In other words, ``employee["name"]`` gets mapped to ``name``, ``employee["gender"]`` to ``gender``, and ``employee["age"]`` to ``age``, 
regardless of their position in the dict!
