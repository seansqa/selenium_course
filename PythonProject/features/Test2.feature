Feature: Add mapping rules
  #Given Navigate to Development Dashboard pageA

#  Scenario: Authentication
#    Given Navigate to Development Dashboard page
#    When Enter Visitor password
#    And Click Log in
#    Then Sign in to Aquanow account
#    Then Enter your Password into Aquanow account
#    Then Select Sign in to Aquanow account
#    Then Generate OTP code
#    Then Click Confirm button

#     # Find transactions with failed mapping status
  Scenario: Filter functionality
    When In Dashboard page
    Then Enter Visitor password
    And Click Log in
    Then Sign in to Aquanow account
    And Enter your Password into Aquanow account
    Then Select Sign in to Aquanow account
    Then Expand Shared Services
    And Select Banking Services
    Then Select Filters
    And Select Remove All
    And Select Add Filter
    Then Click Columns dropdown
    And Choose Mapping Status from Column dropdown
    Then Click Value dropdown
    And Choose "Failure" from Value dropdown
    #Then Close the Filters tab



