  # Homework 6
Feature: eBay.com regression
  # WHILE LOOP
  Scenario: Filter validation - iPhone - multipages Network validation
    Given Go to eBay.com
    When In search-field type "iPhone"
    And Click the "Search" button
    Then Filter "Network" by "Unlocked"
    Then Every item is "Unlocked" for first "2" pages

    Scenario Outline: Filter validation - iPhone - Network
    Given Go to eBay.com
    When In search-field type "<good>"
    And Click the "Search" button
    Then Filter "<filter_name>" by "<filter_value>"
    Then Every item is "<filter_value>"

    Examples: iPhone
      | good   | filter_name | filter_value |
      | iPhone | Network     | Unlocked     |
      | iPhone | Network     | AT&T         |

    Examples: dress
      | good   | filter_name  | filter_value  |
      | dress  | Brand        | Anthropologie |
      | dress  | Dress Length | Long          |
      | dress  | Price        | Under $13.00  |
      | dress  | Color        | Black         |
      | dress  | Size         | M             |

    #  'Color'  and  'Size' are failing due to this errors:
    #   Unable to locate element: {"method":"xpath","selector":
    #   "//li[@class = 'x-refine__main__list'][.//div[text() = 'Color']]//div[@class = 'x-refine__select__svg']
    #   [.//span[text() = 'Black']]//input"}
    #and
    #   "//li[@class = 'x-refine__main__list'][.//div[text() = 'Size']]//div[@class = 'x-refine__select__svg']
    #   [.//span[text() = 'M']]//input"}