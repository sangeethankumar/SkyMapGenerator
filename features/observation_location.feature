Feature: Set observation location parameters

  @skip
  Scenario: Verify that the observation time is set correctly
    Given the observing date is "2023-12-14 22:00:00"
    When the user asks for observation parameters
    Then the date is "2023-12-14"
    And the time is "22:00:00"

  @skip
  Scenario: Verify that the latitude is set correctly
    Given the latitude is 40.7128 degree
    When the user asks for observation parameters
    Then the latitude is 40.7128 degree

  @skip
  Scenario: Verify that the longitude is set correctly
    Given the longitude is -74.0060 degree
    When the user asks for observation parameters
    Then the longitude is -74.0060 degree
