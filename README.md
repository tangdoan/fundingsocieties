
# API and Web UI testing using pytest #
This directory contains two parts of an automation testing solution with API testing and Web UI selenium webdriver testing. Both of them are using pytest framework.
## Table of contents
* [Part1: API automaton testing](#part1:-api-automation-testing)
    * [General requirements](#general-requirements)
    * [Description](#description)
    * [Solution](#solution)
    * [Setup](#setup)
    * [Limitation](#limitation)
* [Part2: Web UI Automation](#part2-web-ui-automation)
    * [Test Scenarios](#test-scenarios)
    * [Solution](#solution)
    * [Setup](#setup)
## Part1: API automaton testing
### General requirements:
    ● Write your code in any programming language of your choice
    ● Create a local git repository like you would in a team setting and push your code
    to GitHub or any other publicly available repository service.
    ● Include instructions for setting up and running your code..
### Description:
1. Use the APIs listed here (https://reqres.in/) and create API automation test suite
2. Automate the above REST API using any automation framework and programming
   language of your choice
### Solution:
API test is created with:
* python version: 3.7.9
* pytest version: 6.1.2
### Setup:
To run this project, install it locally:
1. Download and install [python](#https://www.python.org/downloads/)
2. Open your terminal and install pytest:
```bash
pip install -U pytest
```
3. Run the API test suite by:
```
3.1 clone the repo by: 
git clone https://github.com/tangdoan/fundingsocieties.git
3.2 go to project directory by:
cd ../fundingsocieties
pytest test_API.py -m "API"
```
4. To run the test in parallel: (maximum = 15)
```
pytest test_API.py -n <number_of_parallelism>
```
5. To run each of test case:
```
pytest -rA -k <test_case_name>
```
Please check the list of test case name as below:
```
test_get_list_users
test_get_single_user
test_single_user_not_found
test_list_resource
test_single_resource
test_single_resource_not_found
test_create_user
test_update_user_using_put
test_update_user_using_patch
test_delete_user
test_register_successful
test_register_unsuccessful
test_login_successful
test_login_unsuccessful
test_delayed_response
```
### Limitation:
Because of the data does not get reflect after creating or deleting or updating,
We are unable to verify the date after that.
For e.g: after creating a single user, we should get the user_id and get single user API again to make sure we created successfully.

## Part2: Web UI Automation:
### Test Scenarios:
```
1. open website "https://fundingsocieties.com/"
2. click on statistics in the top navigation bar
3. verify total funded, no of financing, default rate and financing fulfillment rate
displayed or not.
4. verify General, Repayment, Disbursement tabs displayed or not
5. go to General tab and get the total approved loans, total amount disbursed and
default rate
6. go to Repayment tab and get total repayment amount, principal amount and
interest amount
7. go to Disbursement tab and store all industry names according percentage
(increasing order)
```
### Solution:
Web UI test is created with:
* python version: 3.7.9
* pytest version: 6.1.2
* Selenium webdriver
### Setup:
To run this project, install it locally (please ignore it if you have already done it in above):
1. Download and install [python](#https://www.python.org/downloads/)
2. Open your terminal and install pytest:
```bash
pip install -U pytest
```
3. Run the UI test suite by:
```
3.1 clone the repo by: 
git clone https://github.com/tangdoan/fundingsocieties.git
3.2 go to project directory by:
cd ../fundingsocieties
pytest test_UI.py -m "UI"
```

### Challenge:
1. API automation:
- The data does not get reflect when we create/update/delete data. So, we are unable to verify an E2E flow for some test scenarios
e.g: test_create_user, test_update_user, test_delete_user
2. Web UI automation:
- Issue: Unable to verify data from the UI in the chart by using XPATH or CSS_SELECTOR
- Solution: Get the API from network tab of devtools in Chrome and store the value. 

Happy testing!
