============
Dates and time
============

Handling dates and times in Python can be done using the built-in ``datetime`` module, which contains the classes we will use in this chapter.

Let's see some examples:

.. code-block:: python
   :linenos:

    # Imagine that today is 2024-may-07

    # 1. Current date and time
    current_datetime = datetime.datetime.now() 
    print(current_datetime) # => 2024-05-07 19:31:55.594238

    # 2. A specific date
    specific_date = datetime.date(2024, 12, 30)
    print(specific_date) # => 2024-12-30

    # 3. A specific time
    specific_time = datetime.time(12, 30, 45)
    print(specific_time) # => 12:30:45

    # 4. Combining date "A" with time "B"
    combined = datetime.datetime.combine(specific_date, specific_time) 
    print(combined) # => 2024-12-30 12:30:45

    # 5. Calculate difference between dates 
    date1 = datetime.date(2023, 5, 6)
    date2 = datetime.date(2023, 6, 1) 
    time_difference = date2 - date1 
    print(time_difference) # => 26 days, 0:00:00

    # 6. Add or subtract amounts of date/time  
    # besides "weeks" added below, you may add
    # more date/time units as arguments, such as "days" or "hours"
    
    current_date = datetime.date.today() # 2024-05-07
    one_week = datetime.timedelta(weeks=1)
    a_week_from_today = current_date + one_week 
    print(a_week_from_today) # => 2024-05-14

    # 7. It's also possible to customize the datetime format, by using some special characters
    current_datetime = datetime.datetime.now()

    # These are the special characters:
    formatted_date = current_datetime.strftime("%Y/%m/%d %H:%M:%S")
    print(formatted_date) # => 2024/05/07 19:35:36


.. note::

    Visit the official source to learn more these special characters at: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

Date and time in diﬀerent timezones
------------------------------------

It's also possible to get date and time info in other parts of the world!

.. code-block:: python
   :linenos:

    import datetime
    from zoneinfo import ZoneInfo, available_timezones

    # The imported available_timezones() function returns a huge set of timezone choices you can choose from, such as "America/New_York" 
    target_timezone = "America/New_York"

    specific_datetime_another_timezone = datetime.datetime(2023, 4, 2, 10, 0, tzinfo=ZoneInfo(target_timezone)
    )
    print(specific_datetime_another_timezone) #=> 2023-04-02 10:00:00-04:00

    my_datetime = datetime.datetime.now() # 2024-05-07 10:41:11.896407 

    current_datetime_another_timezone = my_datetime.replace(
    tzinfo=ZoneInfo(target_timezone)
    )

    print(current_datetime_another_timezone) # => 2024-05-07 10:41:32.795124-04:00

Pendulum: a third-party alternative
------------------------------

Apart from the built-in ``datetime`` module, "Pendulum" is an interesting third party library to handle dates and time. 
It's deﬁnitely worth checking it out at https://pendulum.eustace.io/.
