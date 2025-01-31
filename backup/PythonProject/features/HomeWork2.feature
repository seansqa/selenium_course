Feature: eBay.com regression
  Scenario: Validate Daily Deals link
    Given Go to eBay.com
    When Locate "Daily Deals" and click
    Then Verify "Deals" page is loaded


  Scenario: Validate "My eBay" dropdown
    Given Go to eBay.com
    When Hover over the "My eBay" dropdown
    And Select "Summary" option
    Then Sign in page opens




  Scenario: Validate Brand Outlet link
    Given Go to eBay.com
    When Locate "Brand Outlet" and click
    Then Verify "Brand Outlet" page is loaded


  Scenario: Validate Gift Cards link
    Given Go to eBay.com
    When Locate "Gift Cards" and click
    Then Verify "eBay eGift Cards" page is loaded

  Scenario: Validate the Help & Contact
    Given Go to eBay.com
    When Locate "Help & Contact" and click
    Then Verify "Help & Contact" page is loaded

  Scenario: Validate the SELL
    Given Go to eBay.com
    When Locate "Sell" and click
    Then Verify "Selling" page is loaded
   # Then captcha navigation


  Scenario: Validate the Watchlist
    Given Go to eBay.com
    When Locate "Watchlist" and click
    Then Verify "sign in" notification is displayed
