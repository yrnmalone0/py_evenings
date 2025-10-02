import datetime as dt

# datetime.date class
current_date = dt.date.today()
print(current_date)
print("Year: ",current_date.year)
print("Year: ",current_date.month)
print("Year: ",current_date.day)

print()

# datetime.time class
current_time = dt.time(12, 58, 43, 00)
print(current_time)
print("Hour: ",current_time.hour)
print("Hour: ",current_time.minute)
print("Hour: ",current_time.second)

print()

# datetime.datetime class
datetime_obj = dt.datetime.now()
print(datetime_obj)
print("Microseconds: ",datetime_obj.microsecond)

print()

# datetime.timedelta class
today_date = dt.datetime.now()
next_year_date = dt.datetime(2026,10,2)

remaining_time = next_year_date - today_date
print(remaining_time)