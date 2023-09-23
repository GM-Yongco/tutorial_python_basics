# Description     : Code that will impress u ;)
# Author          : G.M. Yongco
# HEADER ------------------------------------------------------------------------------------------
import os
from bs4 import BeautifulSoup as bs
from urllib.request import Request, urlopen, urlretrieve

def get_html(url = "https://chihuahuaspin.com/"):
	request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
	page = urlopen(request_site)

	html = (page.read().decode(("utf-8")))
	html = (str)(html.encode('utf-8'))

	return html

def write(the_list):
	the_file = open("ZZ_Manga_links.txt", "w")
	the_file.write(str(the_list))
	the_file.close

def check_if_exist(x:str):
    if not(os.path.exists(x)):
        # need to restart the terminal to update it for some reason
        print(f"Create directory: '{x}'")
        os.mkdir(x)
    else:
        print(f"'{x}' Directory already exists")

def main():
	chapter_number = 4

	html = get_html(f"https://blame-manga.com/manga/blame-chapter-{chapter_number}/")
	# note, fix possible future error
	# ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host

	html = bs(html, "html.parser")

	# prints the first instance of a tag ---------------------------------------
	tag = html.find("title").string
	print(f"PAGE TITLE :{tag}")
	
	# getting the image tags --------------------------------------------------
	image_tags = html.find_all("img")
	write(image_tags)
	print(f"image number {len(image_tags)}")

	# saving images -----------------------------------------------------------
	directory = f"00_Scraped/Blame_Chapter{chapter_number:03d}"
	check_if_exist(directory)

	count = 1
	for line in image_tags:
		print(directory)
		src = line.get("src")

		urlretrieve(src, f"00_Scraped/Blame_Chapter{chapter_number:03d}/Blame_{count:02d}.png")
		count += 1

if __name__ == '__main__':
	print("\nSTART ----------------------------------------")
	main()

	print("\nEND ------------------------------------------")