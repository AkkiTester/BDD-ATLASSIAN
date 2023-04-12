Feature: Atlassian Login Test Check Eamil Valdidation

  Scenario Outline: Login email id Validation with Multiple Parameters
    Given launch chrome browser for login test
    When open Atlassian Login Screen for login test
    And Enter Email "<email>" validation
    Then verify email valid for login

    Examples:
      | email                  |
      | akashdilwale@gmail.com |
      | akash@gmail.com        |
      | akas@bd.com            |
      | dilwale@t.com          |