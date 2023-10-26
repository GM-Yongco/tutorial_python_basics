import datetime

stringy = "8:00"


now = datetime.datetime.now()
today_year = int(now.strftime("%Y"))
today_month = int(now.strftime("%m"))
today_day = int(now.strftime("%d"))

now_str = now.strftime("%H:%M:%S")

x = datetime.datetime(today_year,today_month,today_day, 
    hour = 8,
    minute = 0)
y = now + datetime.timedelta(days=5, hours=-5)

print(f"custom made time: \n{x}\n\n")

print(f"time now:\n{now}\nnow formatted:\n{now_str}\n\n")

print(f"time 5 days and 5 hours from now:\n{y}\n\n")
# note to self: there are no negative hours