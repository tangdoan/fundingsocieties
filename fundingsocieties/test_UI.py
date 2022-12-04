import logging

import pandas as pd
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.quit()


@pytest.mark.UI
def test_fundingsocieties(setup):
    logging.info("\nStep1: open website https://fundingsocieties.com/")
    driver.get("https://fundingsocieties.com/")

    logging.info("\nStep2: click on statistics in the top navigation bar")
    driver.find_element(By.XPATH, "//nav[@class = 'nav-menu']//a[contains(text(),'Statistics')]").click()

    logging.info("\nstep3: verify total funded, no of financing, default rate and financing fulfillment rate "
                 "displayed or not")
    assert driver.find_element(By.XPATH, "//div[contains(text(),'Total funded')]//preceding::font")
    assert driver.find_element(By.XPATH, "//div[@class='detailCaption' and text()='No. of']//preceding::font[1]")
    assert driver.find_element(By.XPATH, "//div[@class='detailCaption' and text()='Default']//preceding::font[1]")
    assert driver.find_element(By.XPATH, "//div[@class='detailCaption' and text()='Financing']//preceding::font[1]")

    logging.info("\nStep4: Verify General, Repayment, Disbursement tabs displayed or not")
    assert driver.find_element(By.XPATH, "//button[contains(text(),'General')]")
    assert driver.find_element(By.XPATH, "//button[contains(text(),'Repayment')]")
    assert driver.find_element(By.XPATH, "//button[contains(text(),'Disbursement')]")

    logging.info("\nStep5: Go to General tab and get the total approved loans, total amount disbursed and default rate")
    driver.find_element(By.XPATH, "//button[contains(text(),'General')]").click()
    # Click Total Approved
    driver.find_element(By.XPATH, "//label[contains(text(),'Total approved')]").click()

    # Data returns from API
    total_approved, amount_disbursed, default_rates, total_repayment_amount, principal_amount, interest_amount, industries = get_data_using_api()
    # Get total approved loans
    logging.info("\nTotal approved loans = {}".format(total_approved))

    # Get Amount Disbursed
    driver.find_element(By.XPATH, "//label[contains(text(),'Amount disbursed')]").click()
    logging.info("\nTotal amount disbursed = {}".format(amount_disbursed))

    # Get Default rates
    driver.find_element(By.XPATH, "//label[contains(text(),'Default rate')]").click()
    logging.info("\nDefault rate = {}".format(default_rates))

    logging.info("\nStep6: Go to Repayment tab and get total repayment amount, principal amount and interest amount")
    driver.find_element(By.XPATH, "//button[contains(text(),'Repayment')]").click()
    logging.info("\nRepayment total = {}".format(total_repayment_amount))

    logging.info("\nRepayment Principal = {}".format(principal_amount))

    logging.info("\nPayment interest = {}".format(interest_amount))

    logging.info("\nStep7: Go to Disbursement tab and store all industry names according percentage")
    driver.find_element(By.XPATH, "//button[contains(text(),'Disbursement')]").click()
    logging.info("\nList of industry names: \n")
    for i in industries:
        value = str(i.get("count")) + "%" + " " + i.get("indsutryname")
        logging.info(value)


def get_data_using_api():
    total_approved_api = "https://api.fundingasiagroup.com/api/fs/p/Wallet/statistics/SG?truncateAmount=false"
    response = requests.get(total_approved_api)
    assert response.status_code == 200
    data = response.json()
    total_approved = data["value"]["number_of_loans"]

    quarter = pd.Timestamp.today().quarter
    current_year = pd.Timestamp.today().year

    amount_disbursed = [x['total_disburse'] for x in data["value"]["loan_amount"] if
                        x['month'] == quarter and x['year'] == current_year]
    amount_disbursed = round(amount_disbursed[0] / 1000000000, 2)

    default_rates = [x['rate'] for x in data["value"]["default_rates"] if
                     x['quarter'] == quarter and x['year'] == current_year][0]

    total_repayment_amount = data["value"]["repayment_received"]
    total_repayment_amount = round(total_repayment_amount / 1000000, 1)

    principal_amount = data["value"]["repayment_principal_received"]
    principal_amount = round(principal_amount / 1000000, 1)

    interest_fee = data["value"]["repayment_late_interest_fee_received"]
    interest_fee = round(interest_fee / 1000000, 2)
    interest_receive = data["value"]["repayment_interest_received"]
    interest_receive = round(interest_receive / 1000000, 2)
    interest_amount = round(interest_fee + interest_receive, 1)

    industries = data["value"]["industries"]
    industries = sorted(industries, key=lambda k: (float(k['count'])), reverse=False)

    return total_approved, amount_disbursed, default_rates, total_repayment_amount, principal_amount, interest_amount, industries
