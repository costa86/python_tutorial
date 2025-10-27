========================
Asynchronous functions
========================

.. image:: https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGV3ZzNlOXJoMXRhZTY1ZDB2dnFhZmExYWZxeDVpZXRtbWF5ZmdqMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/k6r6lTYIL9j9ZeRT51/giphy.gif
   :alt: Description of the animation
   :width: 400px
   :align: center



This concept assumes you have read Functions, Loops, Lists, and Modules chapters.
Async functions in Python, also known as asynchronous functions, are a way of performing tasks concurrently without blocking the execution of other tasks.

As an example, we will simulate downloading something from the web, since this is a task that in reality might take a while to be ﬁnished, 
depending on the internet speed and other circumstances. And at the same time, perform a second task, without having to wait for the ﬁrst task to be ﬁnished. 
We will use the ``asyncio`` built-in library for that.

.. code-block:: python
   :linenos:

    import asyncio
    import random


    async def download_file(file_name: str) -> None:
        print(f"Starting to download {file_name}")
        random_time_to_wait = random.randint(1, 5)
        await asyncio.sleep(random_time_to_wait)
        print(f"Finished downloading {file_name}")


    async def perform_other_task(task_name: str) -> None:
        print(f"Starting {task_name}")
        random_time_to_wait = random.randint(1, 3)
        await asyncio.sleep(random_time_to_wait)
        print(f"Finished {task_name}")


    async def main():
        download_task = asyncio.create_task(download_file("example_file.txt"))
        other_task = asyncio.create_task(perform_other_task("other_task"))

        await download_task
        await other_task


    asyncio.run(main())

Output:

.. code-block:: console

    Starting to download example_file.txt 
    Starting other_task
    Finished downloading example_file.txt 
    Finished other_task


As you can see, in order to make a function asynchronous, the ``async`` keyword must be placed right before ``def``. 
Both ``download_ﬁle()`` and ``perform_other_task()`` functions simulate some time-consuming tasks, by using the ``await asyncio.sleep()`` syntax. 
The ``main()`` function then creates two tasks (``download_task`` and ``other_task``) using ``asyncio.create_task()`` and then awaits for their completion.

To trigger the tasks, the ``asyncio.run()`` function is called with the ``main()`` async function as its argument.

Both tasks will be executed concurrently, allowing the program to perform the other task without waiting for the pseudo-download task to ﬁnish. 
Try running the program multiple times and you will see that order of the outputs will vary, which demonstrates the asynchronous capability of the ``asyncio`` library. 

It’s also worth mentioning that ``random.randint(x, y)`` is a function that returns a random integer between **x-y** each time it’s called. 
We used it in both tasks to simulate the execution time of each one.

The ``await`` keyword signals something that will be waiting to be ﬁnished before the program continues its execution. 
This is what is represented by ``await download_task`` and ``await other_task``.
