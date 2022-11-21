# E-Commerce Web Scraper

Overview: <br/>
Web Scraper with the goal of scraping websites where anti-web scraping mechanics may have been implemented to block common HTTP libraries such as Python's Requests library. Currently capable of scraping Costco's website for all listed laptops. Primarily uses **Python** and **Flask** to create dynamic web pages for displaying scraped data. Utilizes **Selenium** and it's **Chrome Webdriver** to automate website navigation which then allows HTML to be scraped. Obtained HTML is parsed through **Beautiful Soup** and reconstructed as individual objects representing each listed item by use of **Regular Expression**.

<br/>

Features: <br/>
-Automate Chrome to bypass anti-web scraping <br/>
-Scrape and parse HTML from target website <br/>
-Extract useful information from parse tree <br/>
-Display obtained data as a separate HTML page <br/>

In Development: <br/>
-Dynamically alter displayed HTML depending on user selections <br/>
-Filter and categorize items for ease of search and navigation <br/>
-Enhance UI
