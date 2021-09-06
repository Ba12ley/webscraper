# #beautifulsoup does not work with dynamically created sites
# import requests
# from bs4 import BeautifulSoup
# # The url to scrape added in tasks.py
# # URL = "https://www.opendatani.gov.uk/dataset?q=defib|AED|defibrilator"
#
#
# def scrape(url):
#     # set the page and use the requests page on the url
#     page = requests.get(url)
#     # create a BeatifulSoup object looking and load the page content and parse
#     soup = BeautifulSoup(page.content, "html.parser")
#     # id="", _class=""
#     results = soup.find(_class="dataset-resources unstyled")
#     print(results)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
def scrape(url):
    options = webdriver.ChromeOptions()
    options.add_argument(" - incognito")
    browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
    browser.get(url)
    timeout = 10

    try:
        WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//ul[@class='dataset-resources unstyled']")
            )
        )
    except TimeoutException:
        print("Timed out")
        browser.quit()

    data_elements = browser.find_element_by_xpath("//ul[@class='dataset-resources unstyled']")

    for data_element in data_elements:
        result = data_element.find_element_by_xpath(".//ul[@class='dataset-resources unstyled']")
        defib_location = result.get_attribute('ul')
        print(defib_location)

