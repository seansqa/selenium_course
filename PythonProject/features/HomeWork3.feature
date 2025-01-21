# Home work 3
Feature: eBay.com regression
  Scenario: Test Daily Deals navigation
    Given Go to eBay.com
    And   Header navigation: click "Daily Deals"
    #     Locate Daily Deals and click
    Then Verify "Deals" page is loaded

  Scenario: Test Brand Outlet navigation
    Given Go to eBay.com
    And   Header navigation: click "Brand Outlet"
    #     Locate Brand Outlet and click
    Then Verify "Brand Outlet" page is loaded

  Scenario: Test Gift Cards navigation
    Given Go to eBay.com
    And   Header navigation: click "Gift Cards"
    Then Verify "eBay eGift Cards" page is loaded

  Scenario: Test Help & Contact navigation
    Given Go to eBay.com
    And   Header navigation: click "Help & Contact"
    Then Verify "Help & Contact" page is loaded

  Scenario: Test Sell navigation
    Given Go to eBay.com
    And   Header navigation: click "Sell"
    Then Verify "Selling" page is loaded

  Scenario: Test Watchlist navigation
    Given Go to eBay.com
    And   Header navigation: click "Watchlist"
    Then Verify "sign in" page is loaded