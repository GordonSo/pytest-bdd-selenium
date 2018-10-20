Feature: Use the website to find restaurants
  So that I can order food
  As a hungry customer
  I want to be able to find restaurants in my area

  Scenario: Search for restaurants in an area
    Given I want food in "AR51 1AA"
    When I search for restaurants
    Then I should see some restaurants in "AR51 1AA"

  Scenario: Search for restaurants in a different area
    Given I want food in "SE1 5RW"
    When I search for restaurants
    Then I should see some restaurants in "SE1 5RW"

  Scenario: Search for restaurants in an invalid area
    Given I want food in an invalid location
    When I search for restaurants
    Then I should see an error message