============
Classes
============

This is a very rich and important concept not only in Python, but in many other programming languages as well. 
They are used to express more functionalities to an entity.

As a real-world analogy, imagine a cake mold. The cakes made with this mold will come out in the same shape as the mold. 
A circle-shaped cake comes from a circle-shaped cake mold, right? Here, the cake mold is a class and the cakes made out of it are what we call instances of a class. 
The shape is an important detail in this analogy, as it's a feature shared by all these cakes (instances), to prove they came from the same cake mold (class).

As seen in the Dictionaries chapter, you may as well represent this concept using a dict, but in a rudimentary way:

.. code-block:: python
   :linenos:

    employee = {
        "name": "michael scott", 
        "position": "regional manager", 
        "age": 46,
        "past lovers": ["jan", "holly", "donna"], 
        "married": False
    }

    # And for the cake mold analogy too: 
    cake_mold = { "shape": "circle", "price": 5.5 }


Think of the ``employee`` variable as an entity that can hold properties, such as "name", "position", "age" and the others. 
Now let's say you wish to create many other employees. You could just create a function to return a dict like the one just presented. 
But in many scenarios, even more capabilities may be desired, such as actions to be performed by this employee. 
This will make more sense in the following example.

With that in mind, let's create another version of ``employee``. But this time using a class instead. 
For the sake of simplicity, I will adopt a new set of features instead:

.. code-block:: python
   :linenos:

    class Employee:
        def __init__(self, name: str, salary: float = 1000.0) -> None: 
            self.name = name
            self.salary = salary 
            self.company = "Dunder Mifflin"

        def __str__(self) -> str:
            return f"Hi, I am {self.name} and I work at {self.company}. My salary is € {self.salary}"

        def promote(self, salary_raise: float) -> float: 
            self.salary += salary_raise
            return self.salary

    employee_1 = Employee("Pam") 
    employee_1.promote(50.0)

    print(employee_1) # => Hi, I am Pam and I work at Dunder Mifflin. My salary is € 1050.0


Alright, there's a lot to unpack here... Let's go over some details of this implementation:

``__init__()``

As you can see, a class can hold functions. This one in particular is automatically called every time a new ``Employee`` is created. 
Notice the “__” (double underscores). This syntax means the function has some "magical" features. 
We'll see more about that later. For now just keep in mind this function is mandatory, otherwise the class will not work as intended.

``self``

Note that this variable is used all over the class. As the name suggests, it means "this employee instance itself".
As a real-world example, imagine two employees: Jim and Dwight. Even though both are employees at the same company, 
they have features that are unique to each of them, such as "name", "home address" and so on. These features belong to the "self", the individual employee.
To represent this very same idea, the ``self`` variable is used in a class. 
Take some time to see all the places where self appears: in the ``init()`` function, and everywhere I access any feature of ``employee_1``, 
by using this new syntax: ``self.<something_related_to_the_employee>``. Also, note that any function, such as ``promote()``, require ``self`` as the first parameter.

.. note::

    You can adopt another variable name instead of "self". But keep in mind that this term is a widely adopted convention, so I suggest you stick to it.

``__str__()``

Another "magical" function. This one is optional, though. Its purpose is to provide an "introduction" when you ``print()`` a particular instance of a class.

``print(employee_1)``

This is the demonstration of the special feature provided by the ``__str__()`` function. Notice that what was printed is exactly the return of this function, 
even though I didn't explicitly call it.

``employee_1.promote(50.0)``

Here I am calling the ``promote()`` function. I only provided the argument 50.0, which updated the value of ``self.salary`` to 1050.0 (1000.0 + 50.0).
But if you examine this function, it also requires the parameter ``self``, although I did not pass it...The self variable is used only internally by a class. 
You don't specify it when you are using the instances of a class. That's the point of using ``self`` to represent the idea of "selfness".

Class is a very complex subject in Python. We are just scratching its surface in the previous example... 
As *cliché* as it sounds, it's only by practicing that it will become more clear to you.

So far, I intentionally came up with some terms about classes with the purpose of making the concepts more relatable to the real world. 
But it's important to know the actual terms to be used and also reinforce the ones already presented:

- **Instance**: The objects created by the class. The ``employee_1`` variable is an instance of the ``Employee`` class.
- **Attributes**: the characteristics you added to the class. In the ``Employee`` class, ``name``, ``salary`` and ``company`` are its attributes.
- **Method**: A function that is defined within a class. The ``__init__()``, ``__str__()`` and ``promote()`` functions are methods of the ``Employee`` class.
- "**Magical" methods**: Python classes have some built-in methods that are automatically called in certain situations. 
  These methods are denoted by double underscores (“__”) at the beginning and at the end of the method's name. 
  These double underscores in Python are also known as "dunder". You can check them all at https://docs.python.org/3/reference/datamodel.html#special-method-names. 
  Don't get overwhelmed by them, though. In most cases you are very likely to only use the mandatory ``__init__()`` one.
- **Constructor**: The ``__init__()`` method, which is responsible for instantiating the class, is also known as "constructor".
- **Property**: This is how the attributes of an instance are referred to when accessed via dot notation. 
  Example: in ``employee_1.name``, ``name`` is a property of ``employee_1``.
- **Dot (.) notation**: The syntax for accessing methods and properties of a class and its instances by using "." (period). 
  This is a very handy feature, as it allows you to easily identify and access all the capabilities of a given class.

Inheritance
--------------

This is an interesting concept in classes whose name is inspired by the concept of inheritance in biology.

In biology, it means the passing of traits from one generation to the next through their genes. 
As a very basic example, If a woman has blue eyes and she gives birth to a boy with blue eyes too, one may say that the boy inherited his eye color from his mother.
In classes, "inheritance" is a way of mimicking this same concept.

.. image:: https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOWR5Nnd2cGU2dmtrdDZud2d2eW82ZjdmNWt4anpkbjI5dGdyejZ2dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aVIyLrzACDKVEoRUu9/giphy.gif
   :alt: Description of the animation
   :align: center
   
---------------------------


If a company has employees, and some of them are salespeople, these salespeople are employees too, right? 
In this situation, it makes sense to represent this idea with a new class ``SalesPerson`` (child), that would inherit from the ``Employee`` (parent) class we 
already created. The immediate beneﬁt here is that we don't have to rewrite the attributes ``name``, ``salary`` and ``company`` for ``SalesPerson``, 
since they all have been inherited from the ``Employee`` parent class, and are automatically available for usage. 
The methods are inherited too. Let's see how it works:

.. code-block:: python
   :linenos:

    class Employee:
        def __init__(self, name: str, salary: float = 1000.0) -> None: 
            self.name = name
            self.salary = salary 
            self.company = "Dunder Mifflin"

        def __str__(self) -> str:
            return f"Hi, I am {self.name} and I work at {self.company}. My salary is € {self.salary}"

        def promote(self, salary_raise: float) -> float: 
            self.salary += salary_raise
            return self.salary


    class SalesPerson(Employee): # Inherits from "Employee"
        def __init__(self, name: str, salary: float = 1000.0, sales: float = 0.0) -> None:
            super().__init__(name, salary) 
            self.sales = sales

        def __str__(self) -> str:
            return f"Hi, I am {self.name} and I am a salesperson at {self.company}. My total in sales is € {self.sales}"

        def make_sale(self, sale_amount: float) -> None: 
            self.sales += sale_amount

    employee_1 = SalesPerson("Andy") 
    employee_1.promote(50.0) 
    employee_1.make_sale(10.0)

    print(employee_1) # => Hi, I am Andy and I am a salesperson at Dunder Mifflin. My total in sales is € 10.0


Let's unpack some new concepts here:

``class SalesPerson(Employee)``

Notice the new syntax here: I added parentheses and placed ``Employee`` inside it. 
This indicates that ``SalesPerson`` will inherit the properties and methods from ``Employee``.

``super().__init__(name, salary)``

This means that I am calling the ``__init__()`` method of the parent class (``Employee``), by passing the ``name``, and ``salary`` arguments that 
I received from the ``__init__()`` method of the child class ``SalesPerson``. 
Notice that now I have a new attribute ``sales`` being passed via the constructor (remember the ``__init__()`` method is known as "constructor") of ``SalesPerson``. 

.. warning::

    Just to be clear, the ``sales`` attribute is exclusive to ``SalesPerson``, and it's **not** available in the parent class ``Employee``! 
    Inheritance is a one-way route, from parent to children.

``__str__(self)``

Another interesting thing happens here. Even though this method is automatically inherited from the parent, I declared it again here. 
The reason is that I have decided to customize it for the ``SalesPerson`` child class. 
With that, the inherited method from the parent is ignored and the one in the child is used instead. 
This procedure is known as "method overriding". See the result in ``print(employee_1)``.

``employee_1.promote(50.0)``

This is just to prove that the method ``promote()`` is available here too.

``make_sale(self, sale_amount: int)``

As expected, you can normally add new methods to a child class.

Multiple inheritance
---------------------

Another capability allowed is multiple inheritance. The same way a child can inherit traits from both their parents, 
the ``SalesPerson`` class could also inherit from a ``Singer`` class, for instance. 
Just add ``Singer`` as a second argument in ``SalesPerson:``.

.. code-block:: python
   :linenos:

    class Employee:
        def __init__(self):
            self.company = "Dunder Mifflin"
            self.salary = 0.0

        def promote(self, salary_raise: float) -> float:
            self.salary += salary_raise
            return self.salary


    class Singer:
        def __init__(self):
            self.instrument = "Banjo"


    class SalesPerson(Employee, Singer):
        def __init__(self):
            Employee.__init__(self)
            Singer.__init__(self)


    sales_person = SalesPerson()

    all_available = dir(sales_person)
    
    all_properties = vars(sales_person)
    
    all_custom_methods = [
        i
        for i in dir(sales_person)
        if callable(getattr(sales_person, i)) and not i.startswith("__")
    ]

    print("Everything available: ", all_available)
    print("All the properties: ", all_properties)
    print("All the custom methods: ", all_custom_methods)


- Notice the way the parents ``Employee`` and ``Singer`` are initiated are a little different in ``SalesPerson``.
- Notice the output of ``vars(sales_person)``. This built-in function is handy to see all the properties in an object.
- ``all_custom_methods`` is a interesting example of what can be done with list comprehension.

See the output:

.. code-block:: console

    Everything available:  ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'company', 'instrument', 'promote', 'salary']
    All the properties:  {'company': 'Dunder Mifflin', 'salary': 0.0, 'instrument': 'Banjo'}
    All the custom methods:  ['promote']


Multilevel inheritance
-----------------------

And it gets more wild! You can create a new ``JuniorSalesPerson`` class that would inherit from both ``SalesPerson`` and ``Employee`` classes vertically. 
The same way a person can inherit traits from their parents and grandparents at the same time:

.. code-block:: python
   :linenos:

    class Employee:
        def __init__(self, name: str):
            self.name = name

        def __str__(self):
            return f"My name is {self.name}"


    class SalesPerson(Employee):
        pass


    class JuniorSalesPerson(SalesPerson):
        pass

    print(JuniorSalesPerson("Clark"))  # => My name is Clark


As seen above, ``JuniorSalesPerson`` inherited the ``__str__()`` method from ``SalesPerson`` which was inherited from ``Employee``.
The flow is like this:

.. code-block:: rst

    JuniorSalesPerson -> SalesPerson -> Employee

.. warning::

    Class inheritance can be an interesting approach to avoid repetition of code, as you can see. On the other side, 
    keep in mind that it can become hard to manage as the complexity of your program increases, so use it wisely!

Composition
---------------------

This is a different approach to handle relationships between classes. 
This style tends to provide more flexibility and reusability, as it separates the responsibilities of the individual classes. 
We will imagine a scenario that can be handled either with inheritance or composition. 
Then we’ll write two possible solutions, so we can compare both approaches.

Dunder Mifflin is a company that sells paper. It was acquired by another company named Saber, which sells printers. 
As a result of the acquisition, now Dunder Mifflin’s salespeople now sell both paper and printers. Let’s see a possible way to represent this using inheritance:

.. code-block:: python
   :linenos:

    class SchruteFarmsSalesPerson:
        """
        I sell beets
        """

        beets = ["Normal Beets", "Money Beets"]


    class SaberSalesPerson:
        """
        I sell printers
        """

        printers = ["Printer C", "Printer D"]


    class DunderMiffinSalesPerson(SaberSalesPerson):
        """
        I sell paper
        """

        def __init__(self, name: str) -> None:
            self.name = name

        papers = ["Paper A", "Paper B"]


    jim = DunderMiffinSalesPerson("Jim")
    dwight = DunderMiffinSalesPerson("Dwight")

    print("Jim", jim.printers) # => Jim ['Printer C', 'Printer D']
    print("Dwight", dwight.papers) # => Dwight ['Paper A', 'Paper B']



What we just did:

``class DunderMiffinSalesPerson(SaberSalesPerson)``

We added ``SaberSalesPerson`` as a parent class to ``DundlerMifflinSalesPerson``. 
Now, every instance of a ``DunderMiffienSalesPerson`` will have the ``printers`` property too. 
With that, we created two instances (``jim`` and ``dwight``), to represent salespeople at Dunder Mifflin, granting them the ``papers`` and ``printers`` properties. 

You may have noticed an extra ``SchruteFarmsSalesPerson`` class too. Dwight, happens to be the owner of Schute farms, so he produces and sells beets too! 
Based on the concepts we just learned about multiple inheritance, we could simply add ``SchruteFarmsSalesPerson`` as a parent class to ``DundlerMifflinSalesPerson`` too, 
so that dwight would inherit the ``beets`` property. Problem solved, right?

.. image:: https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDY0bDQ3cWZzYnM0Nnhka2NvcWd1OTl3a3FiMTJmYjFvdzFxaDdwaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/etQm5iUnw2wfDct36j/giphy.gif
   :alt: Description of the animation
   :align: center
   
---------------------------


The issue is that if we do this, not only dwight, but all other instances of ``DundlerMifflinSalesPerson``, including ``jim``, would inherit ``beets`` too, 
which would not be accurate, since only Dwight sells beets…

Let’s see another solution, this time using composition:

.. code-block:: python
   :linenos:

    class Product:
        # See about “pass” in the Error/Exception handling chapter. For now, think of it as just a placeholder without any action.   
        pass

    class Beet(Product):
        """
        From Schrute farms
        """
        pass

    class Printer(Product):
        """
        From Saber company
        """
        pass

    class Paper(Product):
        """
        From Dunder Mifflin company
        """
        pass

    class SalesPerson:
        """
        I sell many products
        """
        def __init__(self, name: str, products: list[Product]):
            self.name = name
            self.products = products


    jim = SalesPerson("Jim", [Paper, Printer])
    dwight = SalesPerson("Dwight", [Paper, Printer, Beet])

    print("Jim", [i.__name__ for i in jim.products]) #=> Jim ['Paper', 'Printer']
    print("Dwight", [i.__name__ for i in dwight.products]) #=> Dwight ['Paper', 'Printer', 'Beet']



Some aspects of the new implementation:

There’s generic ``Product`` class, that was used as a parent to generate more categories of products from, as new classes: ``Beet``, ``Paper`` and ``Printer`` 
Also now we have a generic ``SalesPerson`` class, with a ``products`` property as a list of ``Product`` instances. 
As a result, now each salesperson can have their own list of products to sell. 
See that ``jim`` and ``dwight`` sell different products now, even though they are instances from the same class!

This isolation of classes using the composition approach tends to make even more sense as the program grows. 
Suppose that now we have to develop a program to manage the warehouse where Dunder Mifflin stores its products. 
Well, we just created a ``Product`` class, that way we can reuse it in this new warehouse program!

.. image:: https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXQycW8zNTZrMmloeGNuY3VkeTdxajB0cGxqYTY0MnBhdHZxemtmbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DOoxEdozTh4DSjKWs0/giphy.gif
   :alt: Description of the animation
   :align: center
   
---------------------------

  
Alternatives to regular classes
--------------------------

As you may have noticed by now, class is indeed a complex subject in Python, and it may become cumbersome sometimes. 
The good news is that there are some easier-to-implement alternatives, also beneﬁting from the capabilities seen in regular classes. 
Let's go over a few of them:

Named tuples
-------------------

Here's how it works:

.. code-block:: python
   :linenos:

    from collections import namedtuple

    Employee = namedtuple("Employee", ["name", "salary"])

    # This function will become a method in Employee. Notice the “self” parameter
    def greet_function(self) -> str:
        return f"My name is {self.name}"

    # Attaching greet_function() as a method to be named “greet”
    Employee.greet = greet_function
    
    employee_1 = Employee("Erin", 1000.0)

    print(employee_1.salary)  # => 1000.0
    print(employee_1.greet())  # => My name is Erin


Some remarks:

``from collections import namedtuple``

Here I am bringing ``namedtuple`` to the scope of the program, so I can use it. This is a concept better explained in the Modules chapter.

``Employee``

This is the equivalent of declaring a class. The ﬁrst argument is the name of the namedtuple itself, 
and the second is a list with strings representing the attributes (``name`` and ``salary``) of the namedtuple. 
Notice that I capitalized it, so it resembles a class (this is not required, though).

``employee_1 = Employee("Erin", 1000.0)``

This is the equivalent of instantiating a class. Note that all the parameters (attributes) are required.

``Employee.greet = greet_function``

As you can see, attaching methods to a namedtuple is slightly different.

``print(employee_1.salary)``

Also, dot notation is allowed. The same way you do with regular classes.

As you may have assumed, there are trade-oﬀs to using namedtuple over regular classes. 
Here's a few aspects of a namedtuple for your consideration before you adopt it:

- **Immutability**: Just like tuples, you **cannot** change the properties of a namedtuple! This can be a good thing if you wish to prevent accidental changes in the “instances”.
- **Efficiency**: They are more lightweight than classes, which result in less computer memory usage. This can become handy if you need to deal with a large quantity of instances.
- **Equivalency to tuples**: If you ``print(employee_1 == ("Erin", 1000.0))``, the result will be ``True``. Even though the comparison is between a namedtuple and a tuple. 
  It’s important to understand this equivalency.

Dataclasses
--------------

Here's another alternative that also provides more simplicity than a regular class:

.. code-block:: python
   :linenos:

    from dataclasses import dataclass

    @dataclass 
    class Employee:
        name: str
        salary: float = 1000.0
        company: str = "Dunder Mifflin"

        def promote(self, amount: float) -> float: 
            self.salary += amount
            return self.salary

    employee_1 = Employee("Phyllis") 
    employee_1.promote(500)

    print(employee_1.salary) #=> 1500.0
    
Notes:

``from dataclasses import dataclass``

Here I am bringing ``dataclass`` to the scope of the program, so I can use it. This is a concept better explained in the Modules chapter.

``@dataclass``

This is a concept demonstrated in the Decorators chapter. For the moment, keep in mind that it is required, 
and it needs to be exactly in the line above the class deﬁnition!

As you can see, no constructor is required in a dataclass class type! You can simply write the attributes inside the class. 
The remaining features are pretty much the same as seen in regular classes.

Overall, dataclasses are an alternative with less boilerplate to write than regular classes, also providing type annotations for the attributes. 
The possible downside here is that regular classes provide more advanced and granular customizations. 
If this is not an issue to you, then dataclass may be a good ﬁt for your program!

Pydantic
---------------

Unlike the previous approaches, this one requires the installation of a third-party library called "Pydantic". 
Learn more about installing these libraries in the Virtual environment chapter.

.. note::

    Personally, I ﬁnd this library to be the best choice for classes in professional projects, since it provides sophisticated mechanisms for data type 
    validation and many other useful customizations. Besides that, it's a library with a high focus on performance, becoming faster at each new version update.


.. warning::

    The following demonstration assumes you are in an activated venv containing the pydantic library installed.

Let's rewrite the Employee class using the Pydantic library:

.. code-block:: python
   :linenos:

    from pydantic import BaseModel 
    from typing import Literal

    class Employee(BaseModel): 
        name: str
        salary: float = 0.0
        branch: Literal["scranton", "buffalo", "stamford", "utica"] 

    employee_1 = Employee(name="creed",branch="scranton", salary=1000.0) 

    print(employee_1) # => name='creed' salary=1000.0 branch='scranton'


How it works:

``from pydantic import BaseModel and from typing import Literal``

Here I am bringing ``BaseModel`` and ``Literal`` to the scope of the program, so I can use it. This is a concept better explained in the Modules chapter.

``branch: Literal["scranton", "buffalo", "stamford", "utica"]``

This means that the instances of the ``Employee`` class **must** take one of these values as branch: "scranton", "buﬀalo", "stamford", "utica". 
If you try to set any other value, it will not be accepted!

In order to learn more about all the features of Pydantic, check out its oﬃcial documentation at https://docs.pydantic.dev/latest/.	
