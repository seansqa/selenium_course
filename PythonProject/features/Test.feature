Feature: eBay.com regression

  Background: start eBay.com
    Given Go to eBay.com

  Scenario: Validate the search functionality
    When In search-field type "iPhone"
    And click the "Search" button
    Then the first result item is "iPhone"

  Scenario: Validate the Dress search functionality
   When In search-field type "Dress"
   And Click the "Search" button
   Then the first result item is "Dress"

  Scenario: Test Daily Deals navigation
    When Header navigation: click "Daily Deals"
    Then Verify Deals title is displayed

#  Scenario: Filter validation - iPhone - Network
#    When In search-field type "iPhone"
#    And Click the "Search" button
#    Then Filter "Network" by "Unlocked"

    #  For Loop
  Scenario: Search functionality - happy path
   When In search-field type "Dress"
   And Click the "Search" button
   Then Item list should have only "dress" related

  Scenario: Filter validation - iPhone - Network
    When In search-field type "iPhone"
    And Click the "Search" button
    Then Filter "Network" by "Unlocked"
    And Every item is "Unlocked"

  Scenario Outline: Filter validation - iPhone - Network
    #Given Go to eBay.com
    When In search-field type "<good>"
    And Click the "Search" button
    Then Filter "<filter_name>" by "<filter_value>"
    Then Every item is "<filter_value>"

    Examples: iPhone
      | good    | filter_name  | filter_value |
      | iPhone  | Network      | Unlocked     |
      | iPhone  | Network      | AT&T         |
#
    Examples: dress
      | good   | filter_name  | filter_value  |
      | dress  | Brand        | Anthropologie |
      | dress  | Dress Length | Long          |
#      | dress  | size         | M             |
#      | dress  | Color        | Black         |
#

  Scenario: Filter validation - iPhone - multipages Network validation
    When In search-field type "iPhone"
    And Click the "Search" button
    Then Filter "Network" by "Unlocked"
    And Every item is "Unlocked" for first "2" pages

  Scenario: Variables game - 1
    Given This is a variable variable1 variable2 variable3

  Scenario: Variables game - 2
    Given This is the text variable
    """
    Text test test test and so on
    """

  Scenario: Variables game - 3
    Given This is a table data
      | Header One  | Header Two |
      | Cell 1_1    | Cell 1_2   |

    # Lesson 8

  Scenario: Filter validation - iPhone - few filters at once
    When In search-field type "iPhone"
    And Click the "Search" button
    Then Filter "Network" by "Unlocked"
    Then Filter "Buying Format" by "Buy It Now"
    Then Filter "Model" by "Apple iPhone 11"
    Then Filter "Storage Capacity" by "256 GB"
    Then Filter "Condition" by "Open box"
    And Every item relates to following filters
      | filter           | option          |
      | Network          | Unlocked        |
      | Model            | Apple iPhone 11 |
      | Storage Capacity | 256 GB          |
      | Buying Format    | Buy It Now      |
      | Condition        | Open box        |

