# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ========================================================================
# MAIN 
# ========================================================================

def selenium_stuff():
	# Path to the Chrome WebDriver. Make sure to download and specify the correct path to your WebDriver.
	driver = webdriver.Chrome()

	# Navigate to Google
	driver.get("https://www.google.com")

	# Find the search bar element and send keys (search query)
	search_box = driver.find_element_by_name("q")
	search_box.send_keys("Your search query", "Ben 10")

	# Example: Retrieve search results
	search_results = driver.find_elements_by_css_selector("div.g")
	for result in search_results:
		print(result.text)

	# Close the browser
	driver.quit()

def main():
	
	selenium_stuff()
	

	print("hi")

def section(x:str = "SECTION"):
	ret_val = f"\n {x} {'-' * (40 - len(x))}\n"
	print(ret_val)

if __name__ == '__main__':
	section("START")
	main()
	section("END")