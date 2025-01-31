Feature: eBay.com regression

  Background: start eBay
    Given Go to eBay.com

  Scenario: Validate the search functionality
    #Given Go to eBay.com
    When In search-field type "iPhone"
    And Click the "Search" button
    Then the result item is "iPhone"

  Scenario: Validate the Dress search functionality
    #Given Go to eBay.com
    When In search-field type "Dress"
    And Click the "Search" button
    Then the result item is "Dress"


  Scenario: Validate "My eBay" dropdown
    #Given Go to eBay.com
    When Hover over the "My eBay" dropdown
    And Select "Summary" option
    Then Sign in page opens

