Feature: eBay.com regression
#Feature: Shopping mall floors
  Background: start eBay.com
    Given Go to eBay.com
    #And Login as Admin ## t
#  Scenario: collect locations
#    Given Go through each floor and collect data on each location

  Scenario: Test Daily Deals navigation
    When Header navigation: click "Daily Deals"
    Then Verify Deals title is displayed
