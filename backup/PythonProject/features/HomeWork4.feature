  # Homework 4
Feature: eBay.com regression
  #Scenario: Filter validation - iPhone - Network
    #Given Go to eBay.com
    #When In search-field type "iPhone"
    #And Click the "Search" button
    #Then Filter "Network" by "Unlocked"


  Scenario: Filter validation - iPhone - by provider
    Given Go to eBay.com
    When In search-field type "iPhone"
    And Click the "Search" button
    Then Filter "Network" by "Verizon"

  Scenario: Filter validation - iPhone - by Storage Capacity
    Given Go to eBay.com
    When In search-field type "iPhone"
    And Click the "Search" button
    Then Filter "Storage Capacity" by "128 GB"


  Scenario: Filter validation - iPhone - by Model - Apple iPhone 12
    Given Go to eBay.com
    When In search-field type "iPhone"
    And Click the "Search" button
    And Filter "Model" by "Apple iPhone 12"
    Then "Apple iPhone 12" page is displayed

  Scenario: Filter validation - iPhone - by Network provider - AT&T, Model - iPhone 13 and Storage Capacity - 1TB
    Given Go to eBay.com
    When In search-field type "iPhone"
    And Click the "Search" button
    And Filter "Network" by "AT&T"
    And Filter "Model" by "Apple iPhone 13 Pro Max"
    And Filter "Storage Capacity" by "1 TB"
    #Then "Apple iPhone 13 Pro Max" page is displayed

  Scenario: Filter validation - iPhone - by Lock Status -Not Specified
    Given Go to eBay.com
    When In search-field type "iPhone"
    And Click the "Search" button
    And Filter "Lock Status" by "Not Specified"


  # Enter steps to find a complex xpath
    # step 1 - "//li[@class = 'x-refine__main__list'][.//div[text() = 'Network']]"
    # step 2 - "//div[@class = 'x-refine__select__svg'][.//span[text() = 'Unlocked']]//input"
    # step 3 - "//li[@class = 'x-refine__main__list'][.//div[text() = 'Network']]//div[@class = 'x-refine__select__svg'][.//span[text() = 'Unlocked']]//input"

    # to avoid ancestor: "//input[@aria-label = 'Google Search'][not(ancestor::div[@style = 'display:none'])]"
