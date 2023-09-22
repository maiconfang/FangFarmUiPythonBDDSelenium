@loginCredentials
Feature: Enter Login Credentials
  Scenario Outline: Validating the successfully login with valid credentials
    Given I navigate to home page
    And I navigate to login home
    When I enter the login as "<login>"
    Then I enter the password as "<password>"
     And I click on the enter button
     And The login of user should be displayed "<userLogged>"
    Examples:
      | login                       | password    | userLogged |
      | joao.ger@maiffarm.com.br 	|	123		  | joao.ger@maiffarm.com.br |