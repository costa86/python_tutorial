import datetime


from zoneinfo import ZoneInfo, available_timezones


target_timezone = "America/New_York"

specific_datetime_another_timezone = datetime.datetime(
    2023, 4, 2, 10, 0, tzinfo=ZoneInfo(target_timezone)
)
print(specific_datetime_another_timezone)  # => 2023-04-02 10:00:00-04:00

my_datetime = datetime.datetime.now()  # 2024-05-07 10:41:11.896407

current_datetime_another_timezone = my_datetime.replace(
    tzinfo=ZoneInfo(target_timezone)
)

print(current_datetime_another_timezone)  # => 2024-05-07 10:41:32.795124-04:00
