# packages from https://pypi.org/project/html2image/
# installed in cmd using 'pip install --upgrade html2image'

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

from html2image import Html2Image
hti = Html2Image()

# screenshot an HTML file
# hti.screenshot(html_file='page.html', css_file='style.css', save_as='page2.png')

# screenshot an URL
hti.screenshot(url='http://www.youtube.com/', save_as='YT.png')
print("Done")