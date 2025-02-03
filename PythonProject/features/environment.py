import os.path
import re
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def before_all(context):
    ...

def before_feature(context, feature):
    context.URL = "https://www.ebay.com/"

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.wait =  WebDriverWait(context.driver, 10)

def before_step(context, step):
    ...

def after_step(context, step):

    if step.status == 'failed':   # or with single quote 'failed'
        # original_step_name = step.name                                # 1st what we did is - string of step sentence
        # all_words = re.findall(pattern:'\w+', original_step_name)     # [] then, step 2 - we broke it down to words
        # step_name = '_'.join(all_words)
        # context.driver.save_screenshot(f"/../failed_screenshots/{step_name}.png")
        # ##context.driver.save_screenshot(f"/../failed_screenshots/{'_'.join(re.findall(pattern:'\w+', step.name))}.png") ## - in 1 line
        # ###in Windows machine should be:(f"\\..\\failed_screenshots\\
        current_location = os.path.dirname(__file__)  # features
        pattern = '\w+'
        all_words = re.findall(pattern, step.name)
        step_name ='_'.join(all_words)
        timestamp = datetime.now()
        final_location = os.path.join(current_location, '..', 'failed_screenshots', f"{step_name}_{timestamp}.png")
        context.driver.save_screenshot(final_location)
    else:
        print(f"{step}: {step.status}")

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
