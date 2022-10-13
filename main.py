import codecs
from urllib.request import urlopen

import re

import requests
import bs4 as bs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import os #allows for directory manipulation
import webbrowser #allows for displaying websites in browsers

#selenium automates browsers
#chromedriver targets chrome

# chrome_options = Options()
# driver = webdriver.Chrome(executable_path=r"C:\Users\Kevin\Downloads\chromedriver_win32.zip\chromedriver.exe", options=chrome_options)

driver = webdriver.Chrome(ChromeDriverManager().install())   #open chrome through driver
driver.get("https://www.costco.ca/laptops.html")    #opens link
# https://www.bestbuy.ca/en-ca/category/laptops-macbooks/20352

target_soup = BeautifulSoup(driver.page_source, 'lxml')  #parses site

# html = urlopen('file:///' + os.path.abspath('test.html')); #reads html from
html = codecs.open("index.html", "r", "utf-8") #same thing
replacement_soup = BeautifulSoup(html, 'lxml')  #parses html file

# html.parser- built-in - no extra dependencies needed
# html5lib - the most lenient - better use it if HTML is broken
# lxml - the fastest
#
# lenient parsing: can interpret inputs that do not match strict formats



# URL = "https://www.bestbuy.ca/en-ca/category/laptops-macbooks/20352"
# page = requests.get(URL)

class Item:
    name = ""
    html = ""
    link = ""
    price = 0
    description = ""
    spec_list = []
    sale = 0
    out_of_stock = False

    def __init__(self, name, html):
        Item.name = name
        Item.html = html


item_list = []


if __name__ == '__main__':
    # print(soup.prettify())

    target_soup.prettify()

    #extracts all items on site
    html_item_list = target_soup.find_all("span", {'class' : 'description'})

    # for i in range(len(html_item_list)):
    #     cur_html = html_item_list[i]
    #     cur_link = re.findall('^href="([^"]*)"$', str(html_item_list[i]))[0]
    #     # item_list[i].name = re.findall(item_list[i].link + '">([^<]*)<', html_item_list[i])
    #     item_list.append(Item(cur_html, cur_link))
    #     print(item_list[i].link)


    items_as_string = ""   #converts items into string awaiting insert to HTML

    #turns list of items into a chunk of html text
    for item in html_item_list:
        items_as_string += str(item) + "\n"

    # print(items_as_string)

    #reads html file
    # with open(r"C:\Users\Kevin\Desktop\Dev\Webscraper\test.html", 'r') as f:

        # f.write(items_as_string)

        # replacement_soup = BeautifulSoup(f.read());

    # replacement_soup.body.append("<body>" + items_as_string + "</body>", 'html.parser')
    replacement_soup.find("head").insert_after("<body>" + items_as_string + "</body>")



    with open(r"C:\Users\Kevin\Desktop\Dev\Webscraper\index.html", 'w') as f:
        new_str = str(replacement_soup.prettify()) #converts soup into string
        new_str = new_str.replace("&lt;", "<") #fixes "<" and ">" in html
        new_str = new_str.replace("&gt;", ">")
        new_str = new_str.replace("</a>", "</a> <br>") #adds some line breaks
        f.write(new_str) #inputs into html file

        driver.quit() #closes chrome driver













