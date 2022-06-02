import requests
import bs4 as bs
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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
    with open(r"C:\Users\Kevin\Desktop\Dev\scrapedCostco.txt", 'w') as f:
        f.write(soup.prettify())


