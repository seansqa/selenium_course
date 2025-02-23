import warnings
from time import sleep
from behave import step
from selenium.webdriver import ActionChains
# from selenium import webdriver  # moved to environment.py
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
#warnings.filterwarnings("ignore", message=".*LibreSSL.*")


# @step('Navigate to Google')
# def test(context):
#     driver = webdriver.Chrome()
#     driver.get('https://google.com')

@step('Go to eBay.com')  # very sensitive
def test(context):
    # import pdb; pdb.set_trace()
    context.driver.get(context.URL)   # navigate to the webpage
    context.driver.implicitly_wait(2)

# @step('Go to aquanow.io')  # very sensitive
# def test(context):
#     # import pdb; pdb.set_trace()
#     context.driver.get('https://admin-dev.aquanow.io/dashboard')   # navigate to the webpage
#     context.driver.implicitly_wait(2)

@step('the first result item is "iPhone"')
def validate_first_result(context):
    result = context.driver.find_element(By.XPATH, "//span[text() = 'Apple iPhone 8 (Great Condition) - (Unlocked, T-Mobile, Verizon, AT&T etc...)']")


@step('the first result item is "Dress"')
def yet_another_first_result(context):
    context.driver.find_element(By.XPATH, "//span[text() = 'All Saints Maisie speckle dress chiffon crepe splatter shift ruffle cream XSmall']")


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
            element[0].send_keys(good)  # or element.send.keys(good) ?
    else:
        raise Exception("search-field not found")


                                        # Explicit Wait

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
                                            # While Loop

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


                                #   Lesson 9a

@step('Every item spec relates to following filters')
def collect_specs_and_check(context):
    expectations_dict = {row['filter']: row['option'] for row in context.table}     # one-line option of ^

    # collect all items from search result
    items = context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@id,'item')]")))

    # placeholder for all errors
    errors = []

    # context.driver.windows_handles   # gives list of ID for every tab / window
    main_page = context.driver.current_window_handle  # gets current page URL

    # loop through each item
    for item in items:
        title = item.find_element(By.XPATH, ".//span[@role = 'heading']").text
        link = item.find_element(By.XPATH, ".//a[@class = 's-item__link']").get_attribute('href')

        # open link and switch to new tab / window
        context.driver.execute_script(f"window.open('{link}')")
        context.driver.switch_to.window(context.driver.window_handles[-1])    # the last one, i.e. the newest

        # collect all specs
        keys = {key.text for key in context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//dt[contains(@class, 'ux-labels')]//span[text()]")))}
        values = {value.text for value in context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//dd[contains(@class, 'ux-labels')]//span[contains(@class, 'ux-textspans')][not(ancestor::span[@data-testid = 'ux-bubble-help'])][not(ancestor::button)][not (ancestor::span[@aria-hidden='true'])]")))}
        item_specs = dict(zip(keys, values))

        ## do the check
        # is_expectation_matched = item_specs.items() <= expectations_dict.items()    # bool  ## this is another option of the code below (lines 239-243)
        # if not is_expectation_matched:
        #     errors.append(f'Item "{title}" not related to the search')

        for k, v in expectations_dict.items():
            if k not in item_specs.keys():
                errors.append(f'Item "{title}" does not have {k} in its specification')
            elif v != item_specs[k]:
                errors.append(f'Item "{title}" has {item_specs[k]} instead of {v}')



        # function to close currently focused tab / window
        context.driver.close()

        # refocus to main screen
        context.driver.switch_to.window(main_page)

    # if any errors caught -> fire exception
    if errors:
        raise Exception('\n'.join(errors))


                                 #   Lesson 9b

@step('Collect item specs')
def collect_specs(context):
    features_keys = context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//dt[contains(@class, 'ux-labels')]//span[text()]")))
    features_values = context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//dd[contains(@class, 'ux-labels')]//span[contains(@class, 'ux-textspans')][not(ancestor::span[@data-testid = 'ux-bubble-help'])][not(ancestor::button)][not (ancestor::span[@aria-hidden='true'])]")))

    # keys = {key.text for key in context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//dt[contains(@class, 'ux-labels')]//span[text()]")))}
    # values = {value.text for value in context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "///dd[contains(@class, 'ux-labels')]//span[contains(@class, 'ux-textspans')][not(ancestor::span[@data-testid = 'ux-bubble-help'])][not(ancestor::button)][not (ancestor::span[@aria-hidden='true'])]")))}
    #item_specs = dict(zip(keys, values))

    text_keys = []
    for key in features_keys:
        text_keys.append(key.text)


    text_values = []
    for value in features_values:
        text_values.append(value.text)

    item_specs = dict(zip(text_keys, text_values))

    print(item_specs)


# @step('Every dress spec relates to following filters')
# def collect_dress_specs_and_check(context):
#     expectations_dict = {row['filter']: row['option'] for row in context.table}
#
#     # collect all items from search result
#     items = context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@id,'item')]")))
#
#     # placeholder for all errors
#     errors = []
#
#     main_page = context.driver.current_window_handle  # gets current page URL
#
#     # loop through each item
#     for item in items:
#         title = item.find_element(By.XPATH, ".//span[@role = 'heading']").text
#         link = item.find_element(By.XPATH, ".//a[@class = 's-item__link']").get_attribute('href')
#
#         # open link and switch to new tab / window
#         context.driver.execute_script(f"window.open('{link}')")
#         context.driver.switch_to.window(context.driver.window_handles[-1])  # the last one, i.e. the newest
#
#     specs_keys = context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//dt[contains(@class, 'ux-labels')]//span[text()]")))
#     specs_values = context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//dd[contains(@class, 'ux-labels')]")))
#
#     text_keys =[]
#     for key in specs_keys:
#         text_keys.append(key.text)
#
#     text_values = []
#     for value in specs_values:
#         text_values.append(value.text)
#
#     item_specs = dict(zip(text_keys, text_values))
#     #print(item_specs)
#     for k, v in expectations_dict.items():
#         if k not in item_specs.keys():
#             errors.append(f'Item "{title}" does not have {k} in its specification')
#         elif v != item_specs[k]:
#             errors.append(f'Item "{title}" has {item_specs[k]} instead of {v}')
#
#         # function to close currently focused tab / window
#     context.driver.close()
#
#     # refocus to main screen
#     context.driver.switch_to.window(main_page)
#
#     # if any errors caught -> fire exception
#
#
#     if errors:
#         raise Exception('\n'.join(errors))

#                    #  Lesson  10 (Hover over)

@step('test flyout menu for option "{menu_option}"')
def test_flyout_menu(context, menu_option):
    sleep(2)
    option = context.wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class = 'vl-flyout-nav__container']//li[.//a[text() = 'Motors']]")))

    action = ActionChains(context.driver)
    action.move_to_element(option).perform()
    sleep(2)


#  Game Cards Pile and Cards Slots
@step('solve the game')
def solve(context):
    cards = context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id = 'cardPile']/div")))
    placeholder = context.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id = 'cardSlots']/div")))

    for card in cards:
        # get the card number
        card_number = card.text  # str
        true_number = int(card_number)
        target_slot = placeholder[true_number-1]

        ActionChains(context.driver).drag_and_drop(card, target_slot).perform()

#  Game Shopping Mall

# @step('Go through each floor and collect data on each location')
# def check_many_filters(context):
#     # import pdb; pdb.set_trace()
#     # for floor in ['ground', 'first', 'second']:
#
#     ground_floor = context.wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id = 'MLOC-stores-ground']")))
#
#     shops_on_floor = context.wait.until(EC.presence_of_all_elements_located((By.XPATH, ".//*[@id = 'MLOC-stores-ground']//polygon")))
#
#
#     # items = context.wait.until(EC.presence_of_element_located((By.XPATH, "// *[ @ id = \"a102\"]")))
#     # // *[ @ id = "MLOC-anchors-ground"]
#     import pdb;
#     pdb.set_trace()
#     print(shops_on_floor)


# Target website

@step('In search-field type in "gift"')
def element_gift(context):
    element = context.driver.find_element(By.XPATH, "//input[@id = 'search']")
    element.send_keys("gift")

@step('Click "Search" icon')
def click_search(context):
    search_icon = context.driver.find_element(By.XPATH, "//button[@aria-label = 'search']")
    search_icon.click()
    sleep(5)

@step('Click shopping for "Him" option')
def select_for_him_button(context):
    #for_him_option = context.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-test = 'navItemTitleComponent']//span[text() = 'Him']")))
    for_him_option = context.driver.find_element(By.XPATH, "//span[text() = 'Him']")
    # action = ActionChains(context.driver)
    # action.move_to_element(for_him_option).perform()
    for_him_option.click()
    sleep(1)


@step('Click "Gifts under $25"')
def select_gift(context):
    gift_under = context.driver.find_element(By.XPATH, "//div[@data-test = 'navItemTitleComponent']//span[text() = 'Gifts under $25']").click()
    #gift_under.click()
    sleep(2)

@step('List all items under $20')
def items_validation(context):
    price_elements = context.driver.find_elements(By.XPATH,
                                         "//div[@data-test = 'product-details']//span[@data-test = 'current-price']") # [Element1, Element2...]

    items_below_20 = []

    for price_element in price_elements:
        price_text = price_element.text.strip()
        if '$' in price_text:
            price_text = price_text.replace('$', '').strip()

            try:
                price = float(price_text)

                if price < 20:
                    item_name = price_element.find_element(By.XPATH, "//div/a[@data-test = 'product-title']").text

                    items_below_20.append({'name': item_name, 'price': price})
            except ValueError:
                continue

    for item in items_below_20:
        print(f"Item: {item['name']}, Price: {item['price']}")

#context.driver.quit()

    #
    # for each in items:
    #     if price not in each.text:
    #         print(each.text)


    #            #AQUANOW project

#  @step('Navigate to Development Dashboard page')
#  def test(context):
#      context.driver.get("https://admin-dev.aquanow.io/dashboard")
# #
# @step('Enter Visitor password')
# def password(context):
#     element = context.driver.find_element(By.XPATH, "//*[@id='bottom-section']/form/label/input")
#     element.send_keys("9tzx9fCp3k9i4o4-4eVDKKUL")
#     sleep(1)
#
# @step('Click Log in')
# def log_in(context):
#     select_log_in = context.driver.find_element(By.XPATH, "//*[@id='bottom-section']/form/div/button").click()
#
# @step('Sign in to Aquanow account')
# def enter_your_username(context):
#     username = context.driver.find_element(By.XPATH, "//*[@id='amplify-id-:r1:']")
#     username.send_keys("seansqa+1@gmail.com")
#     sleep(1)
#
# @step('Enter your Password into Aquanow account')
# def enter_your_password(context):
#     password_field = context.driver.find_element(By.XPATH, "//*[@id='amplify-id-:r4:']")
#     password_field.send_keys("Telu$008Canad@")
#     sleep(1)
#
#
# @step('Select Sign in to Aquanow account')
# def sign_in(context):
#     signin = context.driver.find_element(By.XPATH, "//*[@id='__next']/div//form/div/button").click()
#    sleep(60)


# Generate OTP code

import base64
import hmac
import hashlib
import struct
import time

# Function to decode the base32 key
def base32_decode(encoded_key):
    return base64.b32decode(encoded_key.upper())

# Function to generate TOTP
def generate_totp(secret_key):
    # Constants
    time_step = 30  # 30 seconds interval for TOTP
    digits = 6  # Length of the OTP (6 digits)

    # Step 1: Get the current timestamp
    timestamp = int(time.time() // time_step)

    # Step 2: Convert timestamp to bytes (big-endian)
    counter = struct.pack(">Q", timestamp)

    # Step 3: Create HMAC-SHA1 hash
    key = base32_decode(secret_key)
    hmac_hash = hmac.new(key, counter, hashlib.sha1).digest()

    # Step 4: Extract the dynamic offset from the hash
    offset = hmac_hash[19] & 0xf

    # Step 5: Extract the 4-byte dynamic code
    code = struct.unpack(">I", hmac_hash[offset:offset + 4])[0] & 0x7fffffff

    # Step 6: Generate OTP by taking the modulus
    otp = code % (10 ** digits)

    # Step 7: Return OTP as a 6-digit string (padded with zeros if necessary)
    return str(otp).zfill(digits)


@step('Generate OTP code')
def otp(context):
    key = "JSE4TEV2RN7SPCUEY255ULZAIJ5QP2OBFZQLU6L6D6FUA6HMH3NA"  # Replace with your actual key
    otp_code = generate_totp(key)
    otp_field = context.driver.find_element(By.XPATH, "//input[@id='amplify-id-:r7:']")
    otp_field.send_keys(otp_code)


@step('Click Confirm button')
def confirm_otp(context):
    confirm_button = context.driver.find_element(By.XPATH, "//button[@type = 'submit']")
    confirm_button.click()
    sleep(1)

#-------------------------------------------------------------------------------------------------------

@step('In Dashboard page')  # very time sensitive
def test(context):
    context.driver.get('https://admin-dev.aquanow.io/dashboard')
    sleep(1)

@step('Enter Visitor password')
def password(context):
    element = context.driver.find_element(By.XPATH, "//*[@id='bottom-section']/form/label/input")
    element.send_keys("9tzx9fCp3k9i4o4-4eVDKKUL")
    sleep(1)

@step('Click Log in')
def log_in(context):
    select_log_in = context.driver.find_element(By.XPATH, "//*[@id='bottom-section']/form/div/button").click()

@step('Sign in to Aquanow account')
def enter_your_username(context):
    username = context.driver.find_element(By.XPATH, "//*[@id='amplify-id-:r1:']")
    username.send_keys("seansqa+1@gmail.com")
    sleep(1)

@step('Enter your Password into Aquanow account')
def enter_your_password(context):
    password_field = context.driver.find_element(By.XPATH, "//*[@id='amplify-id-:r4:']")
    password_field.send_keys("Telu$008Canad@")
    sleep(1)

@step('Select Sign in to Aquanow account')
def sign_in(context):
    signin = context.driver.find_element(By.XPATH, "//*[@id='__next']/div//form/div/button").click()
    sleep(10)

# Enter OTP code manually

@step('Expand Shared Services')
def shared_services_item(context):
    shared_services = context.driver.find_element(By.XPATH, "//div//span[text() = 'Shared Services']")
    shared_services.click()

@step('Select Banking Services')
def sidebar_item(context):
    banking_services = context.driver.find_element(By.XPATH, "//div//span[text() = 'Banking Services']")
    banking_services.click()
    sleep(3)

@step('Select Filters')
def filter_item(context):
    filter_button = context.driver.find_element(By.XPATH, "//button[@id = ':r3t:'][@aria-label = 'Show filters']")
    filter_button.click()
    sleep(1)

@step('Select Remove All')    #to clear filter
def clear_filter(context):
    remove_all = context.driver.find_element(By.XPATH, "//button[text() = 'Remove all']")
    remove_all.click()
    sleep(3)

@step('Select Add Filter')
def add_filter(context):
    add_to_filter = context.driver.find_element(By.XPATH, "//button[text() = 'Add filter']")
    add_to_filter.click()
    sleep(1)

@step('Click Columns dropdown')
def columns_dropdown(context):
    columns = context.driver.find_element(By.XPATH, "//div[@id=':r3u:']/div//div[1]/div[3]")
    columns.click()
    sleep(1)

@step('Choose Mapping Status from Column dropdown')
def choose_mapping_status(context):
    mapping_status = context.driver.find_element(By.XPATH, "//*[@id=':r4p:']/option[8]")
    mapping_status.click()
    sleep(2)

 # Find transactions with failed mapping status
@step('Click Value dropdown')
def value_dropdown(context):
    value = context.driver.find_element(By.XPATH, "//*[@id=':r3u:']//div[1]/div[5]/div")
    value.click()
    sleep(1)

@step('Choose "Failure" from Value dropdown')
def choose_failure(context):
    value_failure = context.driver.find_element(By.XPATH, "//div[@class = 'css-1rh95vz']//*/option[3]")
    value_failure.click()


# @step('Close the Filters tab')
# def close_filter(context):
#     filters_tab = context.driver.find_element(By.XPATH, "//button[@aria-label = 'Delete']//*[@data-testid = 'CloseIcon']")
#     filters_tab.click()





# import ssl
# print(ssl.OPENSSL_VERSION)
#
# import requests
# response = requests.get('https://www.google.com')
# print(response.status_code)

#
# Error: No such keg: /opt/homebrew/Cellar/libressl
# ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'

# # Under QR code (a new one): AIM6HE265C4OXFLDGU3P43MMOVAGPJRHPLEFPTE4UCJNUGY66A4Q

# import pdb
# pdb.set_trace()