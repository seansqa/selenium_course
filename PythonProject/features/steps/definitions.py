import warnings
from time import sleep
from behave import step
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@step('Go to eBay.com')  # very sensitive
def test(context):
    context.driver.get(context.URL)   # navigate to the webpage
    context.driver.implicitly_wait(2)


# @step('In search-field type "{good}"')
# def test_def(context, good):
#     element = context.driver.find_element(By.ID, "gh-ac")  # search for some element
#     element.send_keys(good)  # selenium function emulating typing

@step('In search-field type "{good}"')
def test_def(context, good):
    element = context.driver.find_elements(By.ID, "gh-ac")  # [Elements] or []
    if element:
            element[0].send_keys(good)
    else:
        raise Exception("search-field not found")




@step('Click the "Search" button')
def main_screen_submit_button(context):
    # search_button = context.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@value = 'Search']")), message='Search button missing')
    search_button = context.driver.find_element(By.XPATH, "//button[@value = 'Search']")
    search_button.click()   # selenium cmd to emulate click


@step('the first result item is "iPhone"')
def validate_first_result(context):
    result = context.driver.find_element(By.XPATH, "//span[text() = 'Apple iPhone SE 4rd (Great Condition) - (Unlocked, AT&T, T-Mobile, Verizon)']")


@step('the first result item is "Dress"')
def yet_another_first_result(context):
    context.driver.find_element(By.XPATH, "//span[text() = 'White House Black Market Sleevless Black Floral Flare Scuba Knit Dress Size 2']")


#   Locate Daily Deals and Click
@step('Header navigation: click "{variable}"')
def header_navigation_click(context, variable):
    context.driver.find_element(by=By.XPATH, value=f"//a[aria-label = '{variable}']").click()
    sleep(3)


@step('Filter "{filter_name}" by "{option}"')
def filter_by_name(context, filter_name, option):
    filter_option = context.driver.find_element(By.XPATH, f"//li[@class = 'x-refine__main__list']"
                                                          f"[.//div[text() = '{filter_name}']]//div[@class = 'x-refine__select__svg']"
                                                          f"[.//span[text() = '{option}']]//input")
    filter_option.click()


@step('This is a {variable} {variable1}')
def test_game(context, variable, variable1):
    print(variable)
    print(variable1)


@step('This is the text variable')
def test_text(context):
    expectation = context.text

    actual_text = context.driver.find_elements()


@step('This is the table data')
def test_data(context):
    actual_data = context.table
    headers  = actual_data.headings

    rows = actual_data.rows

    print(headers)
    print(rows)


@step('Every item is "{condition}"')
def items_validation(context, condition):
    items = context.driver.find_elements(By.XPATH,
                                         "//li[contains(@id, 'item')]//span[@role = 'heading']") # [Element1, Element2...]

    for each in items:
        if condition not in each.text:
            print(each.text)


@step('Every item is "{condition}" for first "{page_num}" pages')
def check_few_pages(context, condition, page_num):

    # where we at
    current_page = context.driver.find_element(By.XPATH, "//ol//a[@aria-current]").text  # '100'

    while int(current_page) <= int(page_num):   # evaluate the statement
        items = context.driver.find_elements(By.XPATH, "//li[contains(@id, 'item')]//span[@role = 'heading']")  # [Element1, Element2...]

        for each in items:
            if condition not in each.text:
                # print(each.text)
                # warnings.warn(each.text)
                raise Exception(f'the item {each.text} is not related to {condition}')



        # action - switch the page
        context.driver.find_element(By.XPATH, "//a[@aria-label = 'Go to next search page']").click()
        sleep(2)

        #recollect the current_page
        current_page = context.driver.find_element(By.XPATH, "//ol//a[@aria-current]").text