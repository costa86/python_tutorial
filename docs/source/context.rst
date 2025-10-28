=================
Context manager
=================

This is a structure used to create a "micro isolation" of resources in Python. 
So that inside this isolated context created, you can ensure these resources are properly acquired/open and released/closed, so that any potential leaks are avoided. 
The keyword used for that is with.

Let's see what it means in a practical example. Imagine you have a database to store information about Dunder Mifflin's employees. 
Let's use Python to retrieve all the records in an "employees" table in the database. 
In this scenario, the database is a resource that needs to be properly opened and closed.

.. code-block:: python
   :linenos:

    import sqlite3

    # Connecting to a database
    with sqlite3.connect("dunder_mifflin_database.db") as connection:
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Retrieve records from the "employees" table
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        for i in employees:
            print(i) # Will print each employee


In this previous example, in order to prevent potential leaks in the database connection, 
the connection is automatically closed at the end of the block delimited by with.

Another example of a resource in this scenario could be a simple text ﬁle. Let's use with as a context manager to ``print()`` 
the contents of a ﬁle, so the ﬁle is opened and closed automatically:

*employees.txt*

.. code-block:: rst

    pam 
    michael 
    jim


*main.py*

.. code-block:: python
   :linenos:

    with open('employees.txt', 'r') as file: 
        content = file.read()
        print(content) # Will print each name in the file
