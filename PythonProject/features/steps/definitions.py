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

@step('the first result item is "iPhone"')
def validate_first_result(context):
    result = context.driver.find_element(By.XPATH, "//span[text() = 'Apple iPhone 8 (Great Condition) - (Unlocked, T-Mobile, Verizon, AT&T etc...)']")


@step('the first result item is "Dress"')
def yet_another_first_result(context):
    context.driver.find_element(By.XPATH, "//span[text() = 'Printed Maxi Dress - Tube Style']")


#   Locate Daily Deals and Click
@step('Header navigation: click "{variable}"')
def header_navigation_click(context, variable):
    context.driver.find_element(by=By.XPATH, value=f"//a[@aria-label = '{variable}']").click()
    #sleep(3)

@step('Verify Deals title is displayed')
def verify_deal_title(context):
    deals_title = context.driver.find_element(By.XPATH, "//a[text() = 'Deals']")



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


# Explicit wait
@step('Click the "Search" button')
def main_screen_submit_button(context):
    search_button = context.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@value = 'Search']")), message='Search button missing')
    # search_button = context.driver.find_element(By.XPATH, "//button[@value = 'Search']")    # without Explicit wait
    search_button.click()   # selenium cmd to emulate click



@step('Filter "{filter_name}" by "{option}"')
def filter_by_name(context, filter_name, option):
    filter_option = context.driver.find_element(By.XPATH, f"//li[@class = 'x-refine__main__list']"
                                                          f"[.//div[text() = '{filter_name}']]//div[@class = 'x-refine__select__svg']"
                                                          f"[.//span[text() = '{option}']]//input")
    filter_option.click()
    sleep(2)


@step('This is a {variable} {variable1}')
def test_game(context, variable, variable1):
    print(variable)
    print(variable1)


@step('This is the text variable')
def test_text(context):
    #print(context.text)
    expectation = context.text  # this text is in Test.feature file
    print(expectation)  #?
    actual_text = context.driver.find_elements().text  # this is actual text to compare with


@step('This is the table data')
def test_data(context):
    actual_data = context.table
    headers  = actual_data.headings

    rows = actual_data.rows

    print(headers)
    print(rows)

# For Loop
@step('Item list should have only "{search_item}" related')
def final(context, search_item):
    items_on_page = context.driver.find_elements(By.XPATH, "//div[@class = 's-item__title']")
    for item in items_on_page:
        if search_item.lower() not in item.text.lower():
            #raise ValueError(f'Item {item.text} does not have "dress"')
            raise Exception(f'Item {item.text.lower()} is not related to {search_item.lower()}')



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


        # Lesson 8

@step('Every item relates to following filters')
def check_many_filters(context):
    expectations_dict = {}   #  {'Network': 'Unlocked', ...}

    expectations = context.table
    for row in expectations:
        key = row['filter']
        value = row['option']
        expectations_dict[key] = value

    #expectations_dict = {row['filter']: row['option'] for row in context.table}  # one-line option of ^above cod^

    # collect all items
    items = context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@id,'item')]")))

    # placeholder for all errors
    errors = []

    # loop through each item
    for item in items:
        item_specification = {}
        # extracts title
        title = item.find_element(By.XPATH, ".//span[@role = 'heading']").text
        buyitnow = item.find_elements(By.XPATH, ".//span[contains(@class, 'BuyItNow')]")
        item_model = item.find_elements(By.XPATH, ".//span[contains(@class, 'Apple iPhone 11')]")
        item_capacity = item.find_elements(By.XPATH, ".//span[@class = '256 GB']")
        open_box = item.find_elements(By.XPATH, ".//span[@class = 'Open box']")

        item_specification['title'] = title
        item_specification['Buying Format'] = buyitnow
        item_specification['Model'] = item_model
        item_specification['Storage Capacity'] = item_capacity
        item_specification['Condition'] = open_box

        if expectations_dict['Network'].lower() not in item_specification['title'].lower():
            errors.append(f"Item '{title}' is not related to {expectations_dict['Network']}")
        elif expectations_dict['Buying Format'] == 'Buy It Now' and not item_specification['Buying Format']:
           errors.append(f"Item '{title}' does not relate to {expectations_dict['Buying Format']}")

        # if expectations_dict['Model'].lower() not in item_specification['title'].lower():
        #     errors.append(f"Item '{title}' is not related to {expectations_dict['Model']}")
        elif expectations_dict['Model'] == 'Apple iPhone 11' and not item_specification['Model']:
            errors.append(f"Item '{title}' does not relate to {expectations_dict['Model']}")

        elif expectations_dict['Storage Capacity'] == '256 GB' and not item_specification['Storage Capacity']:
            errors.append(f"Item '{title}' does not relate to {expectations_dict['Storage Capacity']}")

        # if expectations_dict['Condition'].lower() not in item_specification['title'].lower():
        #     errors.append(f"Item '{title}' is not related to {expectations_dict['Condition']}")
        elif expectations_dict['Condition'] == 'Open box' and not item_specification['Condition']:
            errors.append(f"Item '{title}' does not relate to {expectations_dict['Condition']}")


    # # if expectation not matching:
        # title moved to errors

    # if any errors caught -> fire exception
    if errors:
        raise Exception('\n'.join(errors))