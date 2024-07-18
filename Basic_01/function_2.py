# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: main discord bot loop
# HEADERS ================================================================

from typing import List
from time import sleep
from typing import Callable

# ========================================================================
# FUNCTIONS
# ========================================================================

def default_func(message:str = "wiwi")->None:
	print(message)

remember:List[int] = []
def another_func()->None:
	if len(remember) == 0:
		remember.append(0)
	else:
		remember.append(remember[-1] + 1)
	out:str = ""
	for items in remember:
		out += str(items) + ","
	print(out)
		

def get_time_loop(func:Callable = default_func, delay_seconds:int = 5):
	time_passed:int = 0
	while True:
		sleep(delay_seconds)
		func()
		print(time_passed)
		time_passed += delay_seconds

# ========================================================================
# FUNCTIONS
# ========================================================================

if __name__ == '__main__':
	get_time_loop(delay_seconds = 1)