# Go to https://docs.python.org/3/library/index.html and save the page to your
# computer (option to use requests to get the page content programatically)
#
# Open the HTML file with BeautifulSoup.
#
# Extract all links (<a> tags) and save their href, title attributes and their
# text in a CSV file. E.g. the following html:
#
# <a href="https://docs.python.org/3/library/intro.html" title="Introduction"
# accesskey="N">next</a>
# will become a row in the csv file:
#
# url,title,text
# https://docs.python.org/3/library/intro.html,Introduction,next

import csv

import requests
from bs4 import BeautifulSoup


URL = "https://docs.python.org/3/library/"
resp = requests.get(URL)
resp.encoding = "utf-8"

soup = BeautifulSoup(resp.text, "lxml")
with open("python_doc_links.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(("url", "title", "text"))
    for tag in soup.find_all("a"):
        href = tag["href"]
        if not href.startswith("http"):
            href = URL + href
        writer.writerow((href, tag.get("title"), tag.text.strip()))
