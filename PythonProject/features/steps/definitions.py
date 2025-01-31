from behave import step
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@step('Navigate to Google')
def test(context):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://www.bbc.com')

@step('Navigate to eBay')
def test(context):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://www.ebay.com')
    # test
    