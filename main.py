import requests
import bs4 as bs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#selenium automates browsers
#chromedriver targets chrome

chrome_options = Options()
driver = webdriver.Chrome("---CHROMEDRIVER-PATH---", options=chrome_options)

driver.get("https://www.bestbuy.ca/en-ca/category/laptops-macbooks/20352")
soup = BeautifulSoup(driver.page_source, 'html.parser')
#lxml is parser

URL = "https://www.bestbuy.ca/en-ca/category/laptops-macbooks/20352"
page = requests.get(URL)

def print_hi(name):
    print(f"Hi, {name}")


if __name__ == '__main__':
    soup = BeautifulSoup(page.text, "html.parser")
    print(soup.prettify())


