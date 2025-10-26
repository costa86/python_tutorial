
============================
Loops
============================

This concept assumes you have read the Conditionals and Lists chapters.
A loop is a control structure that allows your program to execute a task repeatedly, stopping only when certain conditions are met. 
The most basic example to demonstrate this concept is iterating the elements in a list.

The ``for`` loop
----------------------

This is a loop style more suitable when you know the number of times a task is to be repeated. 
In the following case I know it will be the same number as the quantity of elements in the list. This subtle detail will become more relevant ahead in this chapter.

.. code-block:: python
   :linenos:

    branches = ["scranton", "buffalo", "stamford", "utica"]

    for i in branches: 
        print(i)

Output:

.. code-block:: console

    "scranton" 
    "buffalo" 
    "stamford" 
    "utica"


The syntax is very straightforward, but it is important to understand what is actually going on.
For each element in ``branches``, I am declaring a variable ``i``, then ``print()`` it. 
There's no problem in using the same variable name for all the elements, because for each element there's a new task repetition cycle (iteration), 
so this variable is re-declared for each element, in every new iteration.

.. note::

    In case you are wondering why I named a variable ``i``, it's a common practice to use single letters in this very speciﬁc context (iterating a collection of elements). 
    But this is a matter of taste, as many people tend to adopt something more descriptive, such as the singular version of the list name. 
    In this case, it could be "branch". Personally, I dislike this approach, since normally these two variable names become very similar, 
    so it gets easy to mistake them. Learn more about these naming practices in the Naming conventions chapter.

Iterating over indexes in a collection
----------------------------------

As seen in the previous example with ``branches``, each iteration returns the value of the element. 
But it's also possible to obtain the indexes along with the values, by using the ``enumerate()`` built-in class:

.. code-block:: python
   :linenos:

    winners = ["dwight", "pam", "angela"]

    for i, v in enumerate(winners): 
        print(f"Index: {i}, Value: {v}")

    # This produces the same output: 
    for x in enumerate(winners):
        print(f"Index: {x[0]}, Value: {x[1]}")

Output:

.. code-block:: console

    Index: 0, Value: dwight 
    Index: 1, Value: pam 
    Index: 2, Value: angela

.. note::

    If the syntax of ``for i, v in enumerate(winners)`` looks unfamiliar to you, this is a concept explained in the Deconstructing chapter. 

.. note::

    You can also use ``enumerate()`` with tuples, sets and dicts.


The ``while`` loop
----------------

Even though I know the number of times this task is to be repeated (a typical use case for the ``for`` loop), 
let's rewrite the example above using the ``while`` loop style, so it's easier to visualize what it does.


.. code-block:: python
   :linenos:

    branches = ["scranton", "buffalo", "stamford", "utica"]
    counter = 0

    while counter < len(branches): 
        print(branches[counter]) 
        counter = counter + 1



As you can see, it became a lot more verbose than the ``for`` example. 
I initiated ``counter`` as 0, and while (for as long as) the value of ``counter`` is less than the quantity of elements in ``branches`` (which is 4), 
the program performs the following tasks:

- ``print()`` the index ``counter`` (0 at this moment) in ``branches``.
- Increments the value of ``counter`` by 1 (0 + 1 = 1).

Then it moves up to the next iteration, maintaining the new updated value of ``counter`` (which just became 1), and repeats both tasks again. 
In other words, ``counter`` starts at 0, then it becomes 1, then 2, then 3...then it stops, because 3 is less than 4 (remember that ``len(branches)`` is 4). 
This signals that the loop is over.

Another way of interpreting the ``while`` loop is like saying: "for as long as this condition is met (``counter`` being less than the quantity of elements in ``branches``), 
perform the following tasks."

.. note::

    Instead of ``counter = counter + 1``, you may write it as ``counter += 1``. It's a shortcut for the same thing and it's more commonly used. 
    See more about this syntax in the Operators chapter.

Let's see a more suitable use case for the ``while`` loop, which is when you don't know how many times a task will be repeated:

.. code-block:: python
   :linenos:

    while True:
        employee_name = input("Employee name: ") 
        if employee_name.lower() == "michael":
            break

    # Whatever you write after the "break" will be ignored by the loop iteration!
    print("Hello, world's best boss!")


Let's analyze the implementation:

``while True``

The ``while`` keyword needs to evaluate a boolean condition. Here, ``True`` is a way of saying that the condition for the loop is already met, 
so the ﬁrst loop iteration can take place.

Now let's see what happens inside the loop (tasks to be performed):

``employee_name = input("Employee name: ")``

The ``input()`` function does something very interesting and useful: it asks (prompts) the program user (you) to interact with it by writing a text. 
This text will become the value of ``employee_name``.

``if employee_name == "michael"``

Here you can see a new keyword: ``break``. It signals that the loop must be exited immediately if this condition is met. 
This is a very important detail, because it means that whatever you happen to write after this keyword will be **ignored** by the loop!

With that concept in mind, the task is to check whether ``employee_name`` is equal to "michael". If so, then the loop is over. 
Otherwise, it moves up to the next iteration.

``print("Hello, world's best boss!")``

This is another important concept to grasp. I don't know how many iterations will be required before you (the user) decide to type "michael"...
you might feel like writing all the other employees’ names as far as I know. So, in theory, this loop could run forever! 
That's the point of using the ``break`` keyword, so the loop can be exited after the condition (``employee_name`` being equals to "michael") is met.

it's only after the loop is over that this ﬁnal ``print()`` will get executed. 
Remember: the program is stuck in an infinite loop, so nothing else happens for as long as the condition is not met!
You may use while with other types too, as long as they are validated as boolean. 
Let’s change the previous function to implement a number of attempts, instead of having an infinite loop:

.. code-block:: python
   :linenos:

    attempts = 3
    counter = 1

    while counter <= attempts:
        print(f"Attempt {counter}/{attempts}")
        employee_name = input("Employee name: ")
        
        if employee_name.lower() == "michael":
            print("Hello, world's best boss!")
            break
        
        counter += 1


In this case, the ``while`` loop requires that ``counter <= attempts``. 
The ``counter`` variable starts at 1, which gives a green light to the ``while`` loop. 
Then ``counter`` is incremented by 1 at each iteration. But if ``employee_name == “michael”``, the loop is exited via the ``break`` keyword. 
If ``counter`` reaches 3, it means the user did not type “michael” after 3 attempts, then the loop is exited too. 
Notice I added a nice message so the user can see the remaining attempts they have.

Continue
----------------- 

Alongside ``break``, ``continue`` is another keyword used to cause interruptions in a loop. 
But in this case, to skip only the current iteration. Let’s see how it works:

.. code-block:: python
   :linenos:

    for name in ["pam", "jim", "michael", "jan", "kelly"]:
        if name.startswith("j"):
            # Move up to the next element right now
            continue
        print(name)


Output:
.. code-block:: console

    pam
    michael
    kelly

In this program, each name in the list is expected to be printed, except if it starts with the letter “j”. 
In this case, the name will be skipped, and the iteration will move up to the next name.

.. note::

    In a way, both continue and break are similar in their nature. While ``break`` exits the whole loop, ``continue`` exits only the current element in the loop. 
    Also, both can be used in ``for`` and ``while`` loops.
