from datetime import datetime

now = datetime.now() 
	
# getting the 10am of today
today_year = int(now.strftime("%Y"))
today_month = int(now.strftime("%m"))
today_day = int(now.strftime("%d"))
TEN_AM = datetime(today_year,today_month,today_day, 
	hour = 10,
	minute = 0)

if(TEN_AM > now):
	response = f"{TEN_AM - now}"
else:
	response = f"-{now - TEN_AM}"

print("\n\nCREATE ---------------------------------------")	
print(f"time till 10 am today{response}")


print((TEN_AM-now).total_seconds())