====================
Generators
====================

This concept assumes you have read the Functions and Loops chapters.
This is a way of dynamically creating values in Python. It's represented by the ``yield`` keyword, which returns an iterator that can be used in a loop.
Its main advantage is allowing you to generate a sequence of values without creating a list or any other collection data type in memory. 
This is particularly useful when working with a large quantity of values or when you only need to generate values on the ﬂy.

Let's see it in action:

.. code-block:: python
   :linenos:

    def generate_many_numbers(number: int): 
        counter = 0
        
        while counter < number: 
            yield counter 
            counter += 1

    generated_numbers = generate_many_numbers(5) 

    print(next(generated_numbers)) # Will yield the first number (0)
    print(next(generated_numbers)) # Then the second one (1)
    print(next(generated_numbers)) # Then the third (2)...


Output:

.. code-block:: console

    0
    1
    2


Let's see what happened there:

Instead of returning a value, calling ``generate_many_numbers()`` will yield (generate) a value. The ``next()`` built-in function is used to iterate through a generator. 
So each call to ``next()`` returns the next generated value. As I only called it three times, it only returned the ﬁrst 3 generated values. 
Calling it more times will return the remaining available values in generated_numbers.
Another way of returning the generated values is treating it as a collection, the same way you do with lists and tuples. 
In this case, all the available values will be generated:

.. code-block:: python
   :linenos:

    def generate_many_numbers(number: int): 
        counter = 0
        
        while counter < number: 
            yield counter 
            counter += 1

    for i in generate_many_numbers(5): 
        print(i)


Output:

.. code-block:: console

    0
    1
    2
    3
    4


Increasing performance
---------------------------

Following, a demonstration to visualize the performance boost that a simple generator can provide. 
In this example, we want the sum of the numbers in a given list. For instance: ``[1, 2, 3]`` should return 6 (1 + 2 + 3). 


.. code-block:: python
   :linenos:

    def get_large_sequence(num: int) -> list[int]:
        return [i for i in range(num)]

    def generate_large_sequence(num: int):
        for i in range(num):
            yield i

    number = 100_000
    sum_large_seq = sum(get_large_sequence(number))
    sum_large_seq_gen = sum(generate_large_sequence(number))

    print(sum_large_seq) # => 4999950000
    print(sum_large_seq_gen) # => 4999950000


Some notes:

``number = 100_000``

The “_” character can be used to improve the visibility of a number. It is equivalent to 100000 (one hundred thousand).  

``sum()``

It’s a built-in function to return the aggregated sum of the numbers in a collection. For instance: ``sum([1, 2, 3])`` returns 6.

``sum_large_seq`` and ``sum_large_seq_gen``

As seen, both functions returned the same number (4999950000).

Now, modify the same program to check the memory usage of the list sequence version:

.. code-block:: python
   :linenos:

    import psutil

    def get_large_sequence(num: int) -> list[int]:
        return [i for i in range(num)]

    # Measure memory usage before getting the sequence
    process = psutil.Process()
    memory_usage_before = process.memory_info().rss / 1024 / 1024  # in MiB

    number = 100_000
    sum_large_seq = sum(get_large_sequence(number))

    # Measure memory usage after getting the sequence
    memory_usage_after = process.memory_info().rss / 1024 / 1024  # in MiB

    # Calculate total memory usage
    memory_usage_total = memory_usage_after - memory_usage_before

    print(f"Memory usage to get {sum_large_seq}: {memory_usage_total} MiB") #=> Memory usage to get 4999950000: 2.36328125 MiB

Explaining:

``psutil``

We imported the built-in ``psutil`` module

``process``

An instance of the ``psutil.Process()`` class

``memory_usage_before`` and ``memory_usage_after``

This is to retrieve the memory consumption in that particular moment (in MiB). We stored them in two moments: before and after obtaining the value of ``sum_large_seq``. 
As a result, we see that obtaining ``sum_large_seq`` used  **2.36328125 MiB**.

Now, modify the program again. This time, using the generated sequence version:

.. code-block:: python
   :linenos:

    import psutil

    def generate_large_sequence(num: int):
        for i in range(num):
            yield i

    # Measure memory usage before generating the sequence
    process = psutil.Process()
    memory_usage_before = process.memory_info().rss / 1024 / 1024  # in MiB

    number = 100_000
    sum_large_seq_gen = sum(generate_large_sequence(number))

    # Measure memory usage after generating the sequence using list comprehension
    memory_usage_after = process.memory_info().rss / 1024 / 1024  # in MiB

    # Calculate memory usage of list comprehension
    memory_usage_total = memory_usage_after - memory_usage_before
    print(f"Memory usage to get {sum_large_seq_gen}: {memory_usage_total} MiB") #=> Memory usage to get 4999950000: 0.0 MiB


As a result, we see that obtaining ``sum_large_seq_gen`` used  **0.0 MiB!** 
The reason for this significant difference is that in the generated version, each value in the sequence was incremented individually to generate the final value, 
whereas in the first sequenced list version, a whole list of 100.000 numbers was created in memory!

You may argue that **2.36328125 MiB** vs **0.0 Mib** doesn’t make much difference, but in other scenarios, 
this subtle detail may drastically influence the speed/performance of a program!

.. image:: https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXo5dHN1OWJoNXhoYzU3dW02dDM5b2FqaWt3czRyb3l0M2N4NmgwMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SW3PNayoSGXao/giphy.gif
   :alt: Description of the animation
   :align: center
   
---------------------------

Built-in generator functions
------------------------------

Python provides some built-in functions that can generate values in a similar to list comprehension, as you’ve seen in the Lists chapter:

- **map()**: applies a function to every element in a collection and returns a new collection with the updated values.
- **filter()**: creates a new collection of elements for which a function returns ``True``.
- **reduce()**: applies an aggregation to sequential pairs of values in a collection and returns a single value.
- **range()**: generates a sequence of numbers within a given range.

.. note::

    The following examples will use lists, but other collection types such as tuples and sets could be used as well.

.. note::

    Technically, ``reduce()`` does not generate values, but rather performs a reduction computation. 
    It’s included here because it’s often mentioned alongside ``map()`` and ``filter()``.

.. code-block:: python
   :linenos:

    from functools import reduce

    names = ["jim", "pam", "michael"]

    # 1. map() 
    # see each generated value
    names_upper_map_generator = map(lambda x: x.upper(), names)
    print(next(names_upper_map_generator))  # => JIM
    print(next(names_upper_map_generator))  # => PAM

    names_upper_comprehension = [i.upper() for i in names]
    names_upper_map = list(map(lambda x: x.upper(), names))

    print(names_upper_comprehension == names_upper_map) # => True

    # 2. filter()
    names_with_letter_a_compr = [i for i in names if "a" in i]
    names_with_letter_a_filter = list(filter(lambda x: "a" in x, names))

    print(names_with_letter_a_filter == names_with_letter_a_compr) # => True

    # 3. reduce()
    from functools import reduce
    numbers = [50, 20, 30]
    sum_of_numbers = reduce(lambda current_value, next_value: current_value + next_value, numbers)
    print(sum_of_numbers) # => 100

    # 4. range()
    for i in range(3):
        print(i) # will print(0), print(1) and print(2)

    # Generator functions can be used with regular functions besides lambda.
    numbers = [2, 3, 5]

    def square(number: int) -> int:
        return number ** 2

    squared_numbers = list(map(square, numbers))
    print(squared_numbers)  # => [4,9,25]


Some notes:

``names_upper_map_generator``

That’s just to demonstrate the generation part. By calling ``next(names_upper_map_generator)`` multiple times you get each generated value. 

``names_upper_map`` and ``names_with_letter_a_filter``

Notice both variables are lists holding the result of all the generated values.

``sum_of_numbers``

Notice that ``reduce()`` needs to be imported. Also, this computation works in a slightly different way, 
where the lambda function expects to receive two parameters (``current_value`` and ``next_value``), and returns their sum. 
The final result is the accumulated sum of all the values in numbers. By the way, I picked “current_value” and “next_value” 
only to demonstrate their roles in the function. Any other names could have been chosen.

``for i in range(3)``

Notice that 3 was not printed. That’s because it is an exclusive interval in this case (remember this concept from the Lists chapter). 
Also, ``range(3)`` received an inclusive 0 as a default first argument. In other words, ``range(1,4)`` would range from 1 until 3, for instance.
