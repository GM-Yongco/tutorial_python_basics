# Description		: Code that will impress u ;)
# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# HEADERS ================================================================

# ========================================================================
# FUNCTIONS 
# ========================================================================


# ========================================================================
# MAIN 
# ========================================================================

def main():	
	raw = rf"killyo\ntherekill"
	raw = raw.replace(rf"\n", "\n")
	print(raw)
	section("2")
	print(raw.strip("kill"))

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