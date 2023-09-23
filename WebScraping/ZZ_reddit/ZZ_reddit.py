# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEDERS =================================================================

import os
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen, urlretrieve


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

	# get the first img with an alt = "Post image"
	# get the url to the iamge

	print("place")

if __name__ == '__main__':
	print("\nSTART ----------------------------------------")
	main()

	print("\nEND ------------------------------------------")