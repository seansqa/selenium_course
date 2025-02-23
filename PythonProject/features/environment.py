import os.path
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

def before_all(context):
    ...

def before_feature(context, feature):
    #context.URL = "https://www.ebay.com/" # comment out to use URLs below when working on Lesson 9 (Scenario: Specs from item page) & others
    #context.URL = "https://www.ebay.com/itm/335761166454?_skw=iphone&epid=7072678310&itmmeta=01JKHGMYADPVV9HW10HGQ5D1AH&hash=item4e2cecd076:g:qIYAAOSwCg1nbw1y&itmprp=enc%3AAQAJAAAAwHoV3kP08IDx%2BKZ9MfhVJKkScOCUl2XLfgKaRRHyEVudBjbC8rBdag1%2B%2ByKPDDak0IbnhlEQAFwg3XQSZZZcnPaokZrmJ6Vt4LKVcjniMAZlW6sVuUFJZz%2Fb2C0P3qLANNv57jJG%2FL7fY3vMAbZNv%2Bc9qfhJ80no%2Bq6sLLxVXCNbPiSm8ddpAq4j6QnCSegz5A%2Fvb%2BbwboJlO749X%2FWMNxLG2RR0DTZ0fHAzFM7%2FiXKRL3u7A4ne99%2FD43k%2BokIcLQ%3D%3D%7Ctkp%3ABlBMUNDl07CcZQ"
    #context.URL =  "https://www.ebay.com/itm/316048103845?_skw=dress&itmmeta=01JKS0QBNF5HAM2YSNCK3F347K&hash=item4995ef59a5:g:hpkAAOSwapdnXJLs&itmprp=enc%3AAQAJAAAA4HoV3kP08IDx%2BKZ9MfhVJKkFhlwUt50hxRQmnqdF6vNAjdZptxt9IaV8%2FKCoPhwZyBe0cYV640bLGjHQc8srtZDVCC9Z9wjepglptcF6ChnbdumqALMWqD%2BBtU%2BpE9FpTb0bTsjvfeqPJW9jYUBfxKheRCLWnYPs6dcvnYiYdv6WZEb260UEYpmUBM%2F5jNNF6atcznvXrbcaqtI4PhsPko35GEZDJJJiHLuEwY4SUnWNma17us77cYqXJJnM9f%2Fu2wUHHq9Xr24JwApE7Mpf7TaTrhJnP4WRd%2BKKO5parOxt%7Ctkp%3ABFBM8LrdoJ5l"
    # import pdb; pdb.set_trace()
    #context.URL = "https://www.elated.com/res/File/articles/development/javascript/jquery/drag-and-drop-with-jquery-your-essential-guide/card-game.html"
    #context.URL = "https://mapplic.com/case-study/retail"
    #context.URL = "https://www.target.com/"
    context.URL = "https://admin-dev.aquanow.io/dashboard"

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.wait =  WebDriverWait(context.driver, 10)

def before_step(context, step):
    ...

def after_step(context, step):

    if step.status == "failed":   # or with single quote 'failed'
        # original_step_name = step.name                                # 1st what we did is - string of step sentence
        # all_words = re.findall(pattern:'\w+', original_step_name)     # [] then, step 2 - we broke it down to words
        # step_name = '_'.join(all_words)
        # context.driver.save_screenshot(f"/../failed_screenshots/{step_name}.png")
        # ##context.driver.save_screenshot(f"/../failed_screenshots/{'_'.join(re.findall(pattern:'\w+', step.name))}.png") ## - in 1 line
        # ###in Windows machine should be:(f"\\..\\failed_screenshots\\{'_'.join(re.findall(pattern:'\w+', step.name))}.png"))
        current_location = os.path.dirname(__file__)  # features
        pattern = r'\w+'                       # regular expression
        all_words = re.findall(pattern, step.name)
        step_name ='_'.join(all_words)         # keeps all words and replaces spaces with _
        timestamp = datetime.now()
        final_location = os.path.join(current_location, '..', 'failed_screenshots', f"{step_name}_{timestamp}.png")
        context.driver.save_screenshot(final_location)
    # else:
    #     print(f"{step}: {step.status}")

def after_scenario(context, scenario):
    context.driver.close()  # closes the window / tab
    context.driver.quit()  # closes the process


def after_feature(context, feature):
    ...

def after_all(context):
    ...


def before_tag(context, tag):
    ...

def after_tag(context, tag):
    ...
