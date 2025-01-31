from selenium import webdriver

def before_all(context):
    ...

def before_feature(context, feature):
    context.URL = "https://www.ebay.com"

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def before_step(context, step):
    ...

def after_step(context, step):
    ...


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
