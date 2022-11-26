import codecs
from urllib.request import urlopen

import re

import requests
import bs4 as bs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import os  # allows for directory manipulation
import webbrowser  # allows for displaying websites in browsers

# GLOBAL Variables
driver = None
target_soup = None
replace_index_soup = None
replace_item_soup = None
item_index = {}  # dictionary that tracks the index of an item based on name
item_list = []  # stores all Item objects


class Item:
    name = ""
    brand = ""
    html = ""
    link = ""
    img = ""
    price = 0
    description = ""
    spec_list = []
    sale = 0  # TBA
    out_of_stock = False  # TBA
    reviews = []  # TBA

    def __init__(self, name, brand, html, link, img, price, description, specs):
        self.name = name
        self.brand = brand
        self.html = html
        self.link = link
        self.img = img
        self.price = price
        self.description = description
        self.specs = specs


def connect_to_target():
    # NOTE
    # selenium automates browsers
    # chromedriver targets chrome

    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())  # open chrome through driver
    driver.get("https://www.costco.ca/laptops.html")  # opens link
    # Bestbuy Link
    # https://www.bestbuy.ca/en-ca/category/laptops-macbooks/20352

    # Option 2
    # chrome_options = Options()
    # driver = webdriver.Chrome(executable_path=r"C:\Users\Kevin\Downloads\chromedriver_win32.zip\chromedriver.exe", options=chrome_options)

    # Option 3: Antiwebscraping Blocked
    # page = requests.get(URL)

    global target_soup
    target_soup = BeautifulSoup(driver.page_source, 'lxml')  # parses site

    index_html = codecs.open("templates/index.html", "r", "utf-8")  # reads local html
    global replace_index_soup
    replace_index_soup = BeautifulSoup(index_html, 'lxml')  # html -> Soup parsing

    # item_html = codecs.open("templates/item.html", "r", "utf-8")
    # global replace_item_soup
    # replace_item_soup = BeautifulSoup(item_html, 'lxml')

    # Option 2
    # html = urlopen('file:///' + os.path.abspath('index.html')); #reads html from

    # NOTE
    # html.parser- built-in - no extra dependencies needed
    # html5lib - the most lenient - better use it if HTML is broken
    # lxml - the fastest
    #
    # lenient parsing: can interpret inputs that do not match strict formats


def create_index_page(item_list):
    page = "\n"

    page += "<div class=\"MainContent\"> \n"

    # turns list of items into a chunk of html text
    for i in range(len(item_list)):

        page += "<a href=\"/item/" + item_list[i].name + "\"> \n"  # creates a get request to flask
        page += "<h3>" + item_list[i].name + "</h3> \n"  # add name to html
        page += "</a> \n"

        page += str(item_list[i].html)  # add item html to html

        page += "\n"  # skip line for formatting

    page += "</div>"

    return page


def insert_index_page(index_page):
    # replacement_soup.body.append("<body>" + items_as_string + "</body>", 'html.parser')
    # replacement_soup.find("body").replace_with(index_page)
    replace_index_soup.body.form.insert_after(index_page)

    with open(r"templates/index.html", 'w') as f:
        index_soup = str(replace_index_soup.prettify())  # Soup -> String

        # fixes "<" and ">" in html
        index_soup = index_soup.replace("&lt;", "<")
        index_soup = index_soup.replace("&gt;", ">")
        # index_soup = index_soup.replace("</a>", "</a> <br>")  # adds some line breaks

        f.write(index_soup)  # inputs into html file


# outputs string containing html code for an item
def create_item_page(item):
    page = "\n"

    page += "<div class=\"ItemContent\"> \n"

    page += "<img src=\"" + item.img + "\"/> \n"

    page += "<div class=\"desc\"> \n"

    page += "<h2>" + item.name + "</h2> \n"

    page += "<p>Brand: " + item.brand + "</p> \n"
    page += "<a href=" + item.link + ">Go To Website</a> \n"
    page += "<h3>Price: <br/> " + item.price + "</h3> \n"
    # page += "<br/> " + item.description + "\n"
    # page += "<br/> " + item.specs + "\n"

    page += "\n"  # skip line for formatting

    page += "</div>"

    return page


def insert_item_page(item_page):

    item_soup = ""
    fresh_soup = ""

    # gets a fresh item page
    with open(r"templates/fresh_item_page.html", 'r', encoding="utf-8") as f:
        new_item_soup = BeautifulSoup(f, 'lxml')
        fresh_soup = str(new_item_soup.prettify())

    # resets item page to prepare for new item
    with open(r"templates/item.html", 'w') as f:
        f.write(fresh_soup)

    with open(r"templates/item.html", 'r', encoding="utf-8") as f:
        replace_item_soup = BeautifulSoup(f, 'lxml')

        replace_item_soup.body.nav.insert_after(item_page)  # insert item page content after nav tag

        item_soup = str(replace_item_soup.prettify())  # Soup -> String

        # fixes "<" and ">" in html
        item_soup = item_soup.replace("&lt;", "<")
        item_soup = item_soup.replace("&gt;", ">")
        # index_soup = index_soup.replace("</a>", "</a> <br>")  # adds some line breaks

    with open(r"templates/item.html", 'w') as f:
        f.write(item_soup)  # inputs into html file

# create Item objects from pure extracted HTML
def extract_data(html_item_list, item_list, i):
    # sale = 0'
    # out_of_stock = False

    cur_item = str(html_item_list[i])  # turns soup to string

    cur_name = re.findall(r'<a.*[\n][\s]*(.*)[\n]', cur_item)[0]  # get name

    cur_brand = re.findall(r'([^\s]*)\s', cur_name)[0]  # get brand

    cur_html = html_item_list[i]  # get html

    cur_link = re.findall(r'href="([^"]*)"', cur_item)[0]  # get link
    # item_list[i].name = re.findall(item_list[i].link + '">([^<]*)<', html_item_list[i])

    driver.get(cur_link)  # opens up link to specific device

    item_soup = BeautifulSoup(driver.page_source, 'lxml')

    # gets product image on page
    item_img_soup = item_soup.find("img", {"id": "RICHFXViewerContainer___richfx_id_0_initialImage"})
    cur_img = re.findall(r'src="([^"]*)"', str(item_img_soup))[0]

    # gets product price on page
    item_price_soup = item_soup.find("span", {"automation-id": "productPriceOutput"})
    cur_price = re.findall(r'>([^<]*)<', str(item_price_soup))[0]

    # gets product description on page
    item_description_soup = item_soup.find("div", {"class": "product-info-description",
                                                   "automation-id": "productDescriptions"})
    cur_description = str(item_description_soup)

    # gets product specifications on page
    # can be further broken down
    item_specs_soup = item_soup.findAll("div", {"class": "product-info-description"})[1]
    cur_specs = str(item_specs_soup)

    # create object
    item_list.append(Item(cur_name, cur_brand, cur_html, cur_link, cur_img, cur_price, cur_description, cur_specs))

    global item_index
    item_index[cur_name] = len(item_list)-1


# item_list = []


def main():
    # print(soup.prettify())

    connect_to_target()

    target_soup.prettify()  # Soup -> String

    html_item_list = target_soup.find_all("span", {'class': 'description'})  # extracts all items on site

    # global item_list
    # item_list = []  # stores all Item objects

    count = 0
    # stores data from html into Item object
    for i in range(len(html_item_list)):
        extract_data(html_item_list, item_list, i)
        count+=1
        if(count == 2):
            break

    index_page = create_index_page(item_list)  # converts items into string awaiting insert to HTML
    insert_index_page(index_page)  # inserts page into html form

    driver.quit()  # closes chrome driver


if __name__ == '__main__':
    main()









