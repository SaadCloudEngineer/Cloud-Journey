import datetime

now = datetime.datetime.now()
print("Current date and time:")
print(now)
print("-----")
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("time: ", now.strftime("%H:%M:%S"))


