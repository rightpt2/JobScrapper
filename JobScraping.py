from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup

#url = input("Whats your url: ")
url = "https://www.python.org"

try:
    html = urlopen(url)

except HTTPError as e:
    print(e)

except URLError:
    print("Server down or incorrect domain")

else:

    rse = BeautifulSoup(html.read(),"lxml")
    if rse.title is None:
        print("Tag not found")
    else:
        print(rse.title.getText())

    tags = rse.findAll("h2", {"class": "widget-title"})
    for tag in tags:
        print(tag)
