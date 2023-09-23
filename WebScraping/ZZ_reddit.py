# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEDERS =================================================================

import os
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen, urlretrieve

# ========================================================================
# CUSTOM FUNCTIONS 
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


def get_html(url = "https://chihuahuaspin.com/"):
	request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
	page = urlopen(request_site)

	html = (page.read().decode(("utf-8")))
	html = (str)(html.encode('utf-8'))

	print(html)

	html = bs(html, "html.parser")

	return html

# ========================================================================
# MAIN 
# ========================================================================

def main():
	reddit_template = "https://www.reddit.com/r/"
	subreddit = "ProgrammerHumor"
	modifier = "/top/?t=week" #top all, hot, or whatevs
	# choices are 
	# "/hot
	# "/new"
	# "/top/?t=hour"
	# "/top/?t=day
	# "/top/?t=week
	# "/top/?t=month
	# "/top/?t=year
	# "/top/?t=all

	complete_url = f"{reddit_template}{subreddit}{modifier}"
	print(complete_url)

	# get the first img with an alt = "Post image"
	# get the url to the iamge


	# ===============================================
	# getting images that are posts 
	# ===============================================
	

	image_links = []
	html = selenium_get(complete_url)
	image_tags = html.find_all("img")

	print(f"number of images: {len(image_tags)}")

	for line in image_tags:
		if line.get("id") == "post-image":
			image_links.append(line.get("src"))

	print(f"number of images that are posts: {len(image_links)}")

	for link in image_links:
		print(link)
		urlretrieve(link, f"00_Scraped/ZZ_reddit.png")
		


if __name__ == '__main__':
	print("\nSTART ----------------------------------------")
	main()

	print("\nEND ------------------------------------------")