============
Enum
============

This concept assumes you have read the Classes chapter.
Short for "enumeration", it's a structure useful for situations where you wish to set diﬀerent possibilities of the same entity.

As an analogy, each employee at a company has a job position. This job position can be one out of multiple possibilities, 
such as salesperson, regional manager, accountant, and so on. Let's call these possibilities "variations".

Let's see an example to make it clear:


.. code-block:: python
   :linenos:

	from enum import Enum

	class JobPosition(Enum): # An enum is a class
		SALESPERSON = "salesperson"
		REGIONAL_MANAGER = "regional manager"
		ACCOUNTANT = "accountant"


	introduction = f"Kevin is an {JobPosition.ACCOUNTANT.value}"

	print(introduction) # => Kevin is an accountant


Let's go over some details:

``from enum import Enum``

Here I am bringing ``Enum`` to the scope of the program, so I can use it. This is a concept better explained in the Modules chapter.

``class JobPosition(Enum)``

As you noticed, a Python enum is a class that inherits from the ``Enum`` built-in class. 
Even though it does not require you to write a constructor, you could customize it. But the default implicit constructor is enough in most cases.

``JobPosition.ACCOUNTANT.value``

Let's read this one backwards so it makes more sense: this means I am selecting the ``value`` property of the ``ACCOUNTANT`` variation of the ``JobPosition`` enum. 
This will return the string "accountant".

.. note::

	The adoption of uppercase letters for the variation names in an enum is a convention.
