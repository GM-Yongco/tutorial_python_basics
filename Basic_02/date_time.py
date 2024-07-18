# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
# srource			: https://www.geeksforgeeks.org/python-datetime-module/#python-time-class
# HEADERS ================================================================

from datetime import datetime, date, time, timedelta
from typing import List

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

# ========================================================================
# FUNCTIONS 
# ========================================================================


# ========================================================================
# TESTS 1
# ========================================================================

def test_date(today:date = date.today())->None:
	
	#default format is <year in number>-<month in number>-<day in number>
	print(today)

	examples:List[str] = []

	# how to format strings nd stuff
	examples.append(today.strftime(fr"%d + %m + %y"))
	examples.append(today.strftime(fr"%D - %M - %Y"))
	examples.append(today.strftime(fr"<%b> <%w> <%M>"))
	# see date_time_notes for more formats
	
	# default time for date is 0:0:0.0
	examples.append(today.strftime(fr"<%H> <%M> <%S>"))

	for example in examples:
		print(example)

def test_time(now:time = datetime.now().time() )->None:

	#default format is <24 hour format>:<minute>:<second>.<milisecond>
	print(now)

	examples:List[str] = []

	# how to format strings nd stuff
	# see date_time_notes for more formats
	examples.append(now.strftime(fr"%H + %S + %M"))
	
	# the site said this is okay but its not working for some reason
	try:
		examples.append(now.strftime(fr"%-H = %-S = %-M"))
	except Exception as e:
		print(e)

	# default date for time is january 1 of 1900
	examples.append(now.strftime(fr"%D - %M - %Y"))


	for example in examples:
		print(example)

def test_date_time(now:datetime = datetime.now())->None:
	#default format is just combines the 
	print(now)

	examples:List[str] = []
	examples.append(now.strftime(fr"%d + %m + %y"))
	examples.append(now.strftime(fr"%D - %M - %Y"))
	examples.append(now.strftime(fr"<%b> <%w> <%M>"))
	examples.append(now.strftime(fr"%H + %S + %M"))

	# also invalid here for some reason
	try:
		examples.append(now.strftime(fr"%-H = %-S = %-M"))
	except Exception as e:
		print(e)

	for example in examples:
		print(example)

def test_date_time_2(now:datetime = datetime.now())->None:
	#default format is just combines the 
	print(now)

	year:int = now.year
	month:int = now.month
	day:int = now.day
	hour:int = now.hour
	minute:int = now.minute
	second:int = now.second
	microsecond:int = now.microsecond

	print(f"{year} - {month} - {day} - {hour} - {minute} - {second} - {microsecond}")


# ========================================================================
# TESTS 2
# ========================================================================

def test_custom_time(now:datetime = datetime.now()) -> None:
	now = now.replace(hour=10, minute=0, second=0, microsecond=0)
	print(now)

def test_time_comparison_1(custom_time:datetime = datetime.now().replace(hour=14, minute=0, second=0, microsecond=0)) -> None:
	now:datetime = datetime.now()

	# the -1 day is probably cuz the hour cant be a negative attribute for some reason
	print(type(custom_time - now))
	print(custom_time - now)
	print(now - custom_time)

	if now>custom_time:
		print("now is bigger than custom time")
	else:
		print("custom time is bigger than now")

def test_time_comparison_2(now:datetime = datetime.now()) -> None:
	print(now)

	# adds the value in time delta
	now = now + timedelta(days = 5, hours= -5)
	print(now)
	now = now + timedelta(seconds = 3600)
	print(now)

def seconds_till(time:datetime = datetime.now().replace(hour=21)) -> None:
	now:datetime = datetime.now()

	difference:timedelta = time - now
	if difference.days < 0:
		difference = now - time
	
	print(difference.seconds)

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	
	test_date()
	section("END test")
	
	test_time()
	section("END test")
	
	test_date_time()
	section("END test")
	
	test_date_time_2()
	section("END test")

	test_custom_time()
	section("END test")
	
	test_time_comparison_1()
	section("END test")
	
	test_time_comparison_2()
	section("END test")

	seconds_till()
	section("END test")
	section("END")