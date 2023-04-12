Feature: Atlassian login screen Atlassian logo

  Scenario: Logo presence on Atlassian Login Page
    Given launch chrome browser
    When open Atlassian Login Screen
    Then verify that the logo present on page
    And close browser
