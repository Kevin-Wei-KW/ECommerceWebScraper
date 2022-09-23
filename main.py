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

soup = BeautifulSoup(driver.page_source, 'lxml')   #parses site

# html.parser- built-in - no extra dependencies needed
# html5lib - the most lenient - better use it if HTML is broken
# lxml - the fastest
#
# lenient parsing: can interpret inputs that do not match strict formats



# URL = "https://www.bestbuy.ca/en-ca/category/laptops-macbooks/20352"
# page = requests.get(URL)


if __name__ == '__main__':
    # print(soup.prettify())

    item_list = soup.find_all("span", {'class' : 'description'})

    items_as_string = ""

    for item in item_list:
        items_as_string += str(item) + "\n"

    print(items_as_string)
    with open(r"C:\Users\Kevin\Desktop\Dev\Webscraper\test.html", 'w') as f:
        f.write(items_as_string)



