# 5 Days back from today
import datetime
today = datetime.date.today()
five_days_back = today - datetime.timedelta(days = 5)

print("5 days back from today is: ", five_days_back.strftime("%A, %b-%d-%y"))



# Date and day from yesterday, today and tomorrow
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)

print("yesterday was: ", yesterday.strftime("%y-%m-%d"))
print("today was: ", today.strftime("%y-%m-%d"))
print("tomorrow was: ", tomorrow.strftime("%y-%m-%d"))



# Date without microseconds
current_time = datetime.datetime.now()
microsecond = current_time.replace(microsecond = 0)

print("Original datetime format: ",current_time)
print("Datetime without microseconds: ", microsecond)



# Difference between two dates in seconds.
date1 = datetime.datetime(2023, 2, 15, 0, 0)
date2 = datetime.datetime(2023, 2, 20, 0, 0)

difference = (date2 - date1).total_seconds()

print("The total difference between two dates in seconds is: ", difference)