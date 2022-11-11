import codecs
import os
from urllib.request import urlopen

import bs4 as bs
from bs4 import BeautifulSoup

# html = urlopen('file:///' + os.path.abspath('test.html')); #reads html from
html = codecs.open("templates/test.html", "r", "utf-8")

replacement_soup = BeautifulSoup(html, 'html.parser')  #parses html file

if __name__ == '__main__':
    print(">" + str(replacement_soup))