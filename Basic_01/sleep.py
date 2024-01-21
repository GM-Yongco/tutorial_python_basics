# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================
import time

# ========================================================================
# MAIN 
# ========================================================================

def main():
	time.sleep(3)
	print("3 seconds have passed")

	for i in range (4, 11):
		time.sleep(1)
		print(f"{i} seconds have passed")

# ========================================================================
# MISC FUNCTIONS
# ========================================================================

def section(x:str = "SECTION"):
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

if __name__ == '__main__':
	section("START")
	main()
	section("END")