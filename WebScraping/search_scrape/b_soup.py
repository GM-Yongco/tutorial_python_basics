# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

from pprint import pprint

from selenium import webdriver

from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen, urlretrieve


# ========================================================================
# SELENIUM 
# ========================================================================

def selenium_get(THE_URL):
	# Initialize a web driver (e.g., Chrome)
	driver = webdriver.Chrome()

	# Load the Reddit page
	driver.get(THE_URL)

	# Wait for the page to load completely (you may need to adjust the wait time)
	driver.implicitly_wait(30)

	# Get the page source after it's fully loaded
	page_source = driver.page_source

	# Close the web driver
	driver.quit()

	# Parse the page source with BeautifulSoup
	soup = bs(page_source, "html.parser")

	print("sel end\n-\n")

	return soup

# ========================================================================
# MAIN 
# ========================================================================

def main():
	# GETTING THE HTML ==========================
	MY_URL = "https://genius.com/search?q=no%20-%20meghan%20trainor"

	bs_html = selenium_get(MY_URL)

	# FINDING THE STUFF I WANT ==================

	group_tag = bs_html.find_all("search-result-items", "results='$ctrl.section.hits'")


	# STORING THE STUFF I WANT ==================

	print(group_tag)

	section("print")

	# for link in links:
	# 	print(link.get("href"))


# ========================================================================
# MISC
# ========================================================================

def section(x:str = "SECTION"):
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

if __name__ == '__main__':
	section("START")
	main()
	section("END")