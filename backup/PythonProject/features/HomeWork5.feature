  # Homework 5
Feature: eBay.com regression
  Scenario: Validate Search-field use multiple words as variable
    Given Go to eBay.com
    And In search-field look for "dress"
    #And Click the "Search" button

  Scenario: Variables game - 1
    Given This is a "variable" "variable1" "variable2"

  Scenario: Text validation
    Given Store below text as a variable
    """
    Text test test test and so on
    """

  Scenario: Validate table
    Given This is the table data
    | Header One | Header Two|
    | Cell 1_1   | Cell 1_2  |
    | Cell 2_1   | Cell 2_2  |

  Scenario: Search functionality - happy path
    Given Go to eBay.com
    And In search-field type "dress"
    And Click the "Search" button
    Then Item list should have only "dress" related
    #

  Scenario: Filter validation - iPhone - Network
    Given Go to eBay.com
    When In search-field type "iPhone"
    And Click the "Search" button
    Then Filter "Network" by "Unlocked"
    Then Every item is "Unlocked"


    #cart = ['apple', 'carrot', 'milk']
    #print('apple')
    #print('carrot')
    #print('milk')

    #for item in cart:
    #print(item)

    #for i in range(20):
   # print(i)
   # Result: 0.1.2.3.4.5.6.7.8.9.10.11.12.13.14.15.16.17.18.19

