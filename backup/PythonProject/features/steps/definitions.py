from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from behave import step
#from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# @step('Navigate to Google')
# def test(context):
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.get('https://www.google.com')

@step('Go to eBay.com') # very sensitive
def test(context):
                                               # starting new browser    # context.driver = webdriver.Chrome()
    context.driver.get(context.URL)            # navigate to the webpage # context.driver.get('https://www.ebay.com')
                                               # maximizes window        #  context.driver.maximize_window()

@step('In search-field type "{good}"')
def test_def(context, good):
    element = context.driver.find_element(By.XPATH, "//input[@aria-label = 'Search for anything']")  # search for some element
    # element = context.driver.find_element(By.ID, "gh-ac")
    element.send_keys(good)  # selenium function emulating typing

# @step('In search-field type "Dress"')
# def search_dress(context):
#    field = context.driver.find_element(By.ID, "gh-ac")
#    field.send_keys("Dress")
#

@step('Click the "Search" button')
def test_another_name(context):
    search_button = context.driver.find_element(By.XPATH, "//button[@value = 'Search']")
    search_button.click()  # selenium cmd to emulate click


@step('the result item is "iPhone"')
def validate_first_result(context):
    result = context.driver.find_element(By.XPATH, "//span[text() = 'Apple iPhone 12 (Excellent Condition) - (Unlocked, AT&T, TMobile, Verizon...etc)']")


@step('the result item is "Dress"')
def yet_validate_first_result(context):
    #result = context.driver.find_element(By.XPATH, "//span[text() = 'Bellamra Dress Womens White Small Italy Lined Maxi Silk Blend Sleeveless Slip']")
    result = context.driver.find_element(By.XPATH, "//span[text() = 'Black floral print dress']")
    sleep(3)


#------------Home Work 2, 3-------------


@step('Locate "Daily Deals" and click')
def test_deals_link(context):
   element = context.driver.find_element(By.XPATH, "//a[@aria-label='Daily Deals' and text()='Daily Deals']")
   element.click()

#      Locate "Daily Deals" and click
@step('Header navigation: click "{variable}"')
def header_navigation_click(context, variable):
    #link = context.driver.find_element(By.XPATH, f"//a[@aria-label='{variable}' and text()='{variable}}']")
    link = context.driver.find_element(By.XPATH, f"//nav//*[@aria-label='{variable}' or text()='{variable}']")
    link.click()
    #context.driver.find_element(By.XPATH, f"//a[@aria-label='{variable}' and text()='{variable}}']").click() - # An option to have Find and Click in one line
    sleep(3)


#@step('Verify "Deals" page is loaded')
#def verify_deals_page(context):
    #result = context.driver.find_element(By.XPATH, "//a[text() = 'Deals']")
@step('Verify "{variable}" page is loaded')
def verify_link_page(context, variable):
    result = context.driver.find_element(By.XPATH, f"//*[text() = '{variable}']")


#------------Homework 4---------------


@step ('Filter "{filter_name}" by "{option}"')
def filter_by_name(context, filter_name, option):
    #filter_option = context.driver.find_element(By.XPATH, f"//li[@class = 'x-refine__main__list'][.//div[text() = '{filter_name}']]//div[@class = 'x-refine__select__svg'][.//span[text() = '{option}']]//input")
    filter_option = context.driver.find_element(By.XPATH, f"//li[@class = 'x-refine__main__list']"
                                                          f"[.//div[text() = '{filter_name}']]//div[@class = 'x-refine__select__svg']"
                                                          f"[.//span[text() = '{option}']]//input")
    filter_option.click()
    sleep(3)

@step('"{option}" page is displayed')
def filter_page_result(context, option):
    sleep(3)
    result = context.driver.find_element(By.XPATH, f"//div[text() = '{option}']")
    sleep(3)


#--------------Homework 5-----------------


@step('In search-field {look_for} "{my_search}"')
def ebay_search(context, look_for, my_search):
    search = context.driver.find_element(By.XPATH, "//input[@aria-label = 'Search for anything']")
    search.send_keys(my_search)
    print(look_for)
    print(my_search)


@step('This is a "{variable}" "{variable1}" "{variable2}"')
def test_game(context,variable, variable1, variable2):
    print(variable)
    print(variable1)
    print(variable2)


@step('Store below text as a variable')
def text_as_a_variable(context):
    print(context.text)
                                                                #or  my_variable = context.text
                                                                #    print(my_variable)
    #expectation = context.text

    #actual_test = context.driver.find_element().text
    ##assert actual_test == expectation
    #actual_test = context.driver.find_elements()

@step('This is the table data')
def test_table(context):
    actual_data = context.table
    headers = actual_data.headings

    rows = actual_data.rows

    print(headers)
    print(rows)

@step('Every item is "{condition}"')
def items_validation(context, condition):
    items = context.driver.find_elements(By.XPATH, "//li[contains(@id, 'item')]//span[@role = 'heading']")  # (Element1, Element2...)

    for each in items:
        if condition not in each.text:   #  returns all 'UNLOCKED' and 'unlocked' items
        #if condition.lower() not in each.text.lower():
            print(each.text)

@step('Item list should have only "{apparel}" related')
def items_validation(context, apparel):
    items = context.driver.find_elements(By.XPATH, "//li[contains(@id, 'item')]//div[@class = 's-item__wrapper clearfix']")

    for each in items:
        #if apparel not in each.text:     # - this code is case-sensitive, may return all upper-case (DRESS) or camel-case (Dress)
        if apparel.lower() not in each.text.lower():
            print(each.text)

    # for item in ['dress', 'iPhone' ]:
    #         print(f'Ebay search for {item}')



#------------------Homework 6---------------


@step('Every item is "{condition}" for first "{page_num}" pages')
def check_few_pages(context, condition, page_num):
    current_page = context.driver.find_element(By.XPATH, "//ol//a[@aria-current]").text     # where we at

    while int(current_page) <= int(page_num):  # evaluate the statement
        items = context.driver.find_elements(By.XPATH,
                                             "//li[contains(@id, 'item')]//span[@role = 'heading']")  # (Element1, Element2...)

        for each in items:
            if condition not in each.text:
               print(each.text)

        # action -switch the page
        context.driver.find_element(By.XPATH, "//a[@aria-label = 'Go to next search page']").click()
        sleep(2)

        # recollect the current_page                                    # ....we need this step to avoid infinite loop
        current_page = context.driver.find_element(By.XPATH, "//ol//a[@aria-current]").text



# goal = 1000000
# bank = 0
#
# salary = 100000
#
# while bank < goal:
#     bank += salary
#     print('worked for whole year')







#____________________________________________________________________________________________________________________
#@step('Locate "Brand Outlet" and click')
#def test_outlet_link(context):
    #element = context.driver.find_element(By.XPATH, "//a[@aria-label='Brand Outlet' and text()='Brand Outlet']")
    #element.click()
    #sleep(3)

#@step('Verify "Brand Outlet" page is loaded')
#def verify_outlet_page(context):
    #result = context.driver.find_element(By.XPATH, "//h1[text() = 'Brand Outlet']")


#@step('Locate "Gift Cards" and click')
#def test_gift_cards_link(context):
    #element = context.driver.find_element(By.XPATH, "//a[@aria-label = 'Gift Cards' and text() = 'Gift Cards']")
    #element.click()
    #sleep(3)

#@step('Verify "eBay eGift Cards" page is loaded')
#def verify_gift_cards_page(context):
    #result = context.driver.find_element(By.XPATH, "//h5[text() = 'eBay eGift Cards']")


#@step('Locate "SELL" and click')
#def test_sell_link(context):
    #element = context.driver.find_element(By.XPATH, "//a[@aria-label = 'Sell' and text() = 'Sell']")
    #element.click()
    #sleep(3)

#@step('Verify "Selling" page is loaded')
#def verify_selling_page(context):
    #result = context.driver.find_element(By.XPATH, "//h1[text() = 'Selling']")
    #sleep(3)


#@step('Locate "Help & Contact" and click')
#def test_help_contact_link(context):
    #element = context.driver.find_element(By.XPATH, "//a[@aria-label = 'Help & Contact' and text() = 'Help & Contact']")
    #element.click()
    #sleep(3)

#@step('Verify "Help & Contact" page is loaded')
#def verify_help_page(context):
    #result = context.driver.find_element(By.XPATH, "//h1[text() = 'How can we help you today?']")
    ##result = context.driver.find_element(By.XPATH, "///h1[text() = 'Please verify yourself to continue']")
    #sleep(3)


#@step('Locate "Watchlist" and click')
#def test_watchlist_link(context):
    #element = context.driver.find_element(By.XPATH, "//span[@class = 'gh-watchlist__target' and text() = 'Watchlist']")
    #element.click()
    #sleep(3)
  # Need to sign in to watch

#@step('Verify "sign in" notification is displayed')
#def verify_sign_in_notification(context):
   ## result = context.driver.find_element(By.XPATH, "//a[contains(text() = 'sign in')]")
   ## result = context.driver.find_element(By.XPATH, "//span[contains(text() = ' to view items you are watching.')]")
    #result = context.driver.find_element(By.XPATH, "//*[contains(@class, 'rvi') and text() = 'Please']")
    #sleep(3)

@step('Header navigation: hover over "{variable}"')
def header_navigation_click(context, variable):
    sleep(2)
    expand_my_ebay_dropdown = context.driver.find_element(By.XPATH, f"//*[text() = '{variable}']")
    actions = ActionChains(context.driver)
    actions.move_to_element(expand_my_ebay_dropdown).perform()
    sleep(2)

@step('Select "{variable}" option')
def select_summary_option(context, variable):
    sleep(3)
    #dropdown_option = context.driver.find_element(By.XPATH, "//option[@value = '{variable}']")
    dropdown_option = context.driver.find_element(By.XPATH, f"//nav//*[@class='gh-my-ebay__list-item']//a[text()='{variable}']")
    dropdown_option.click()


@step('Hover over the "My eBay" dropdown')
def my_ebay_dropdown(context):
    sleep(3)
    expand_my_ebay_dropdown = context.driver.find_element(By.XPATH, "//span[text() = 'My eBay']")
    actions = ActionChains(context.driver)         # Hover over the dropdown element to display the options
    actions.move_to_element(expand_my_ebay_dropdown).perform()    # hover over to select from the drop-down
    sleep(3)

#@step('Select "Summary" option')
#def select_summary_option(context):
    #sleep(3)
    #dropdown_option = context.driver.find_element(By.XPATH, "//li[@class='gh-my-ebay__list-item']//a[text()='Summary']")
    #dropdown_option.click()

# @step('Captcha page opens')
# def capcha_page_result(context):
  #  sleep(3)
  #  result = context.driver.find_element(By.XPATH, "//h1[text()='Please verify yourself to continue']")
  #  assert result.is_displayed(), "Please verify yourself to continue"

@step('Sign in page opens')
def sign_in_page_result(context):
    sleep(3)
    result = context.driver.find_element(By.XPATH, "//h1[text()='Sign in to your account']")
    assert result.is_displayed(), "Sign in to your account"