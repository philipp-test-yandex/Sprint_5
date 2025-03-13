from conftest import driver
from helpers.locators import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, PERSONAL_ACCOUNT_BUTTON
from helpers.constants import URL_HOME_PAGE
import time

user_email = 'filipp_aslapov_19_015@mail.ru'
user_pass_succes_reg = 'Pass123'

def test_click_through_personal_account(driver):
    driver.get(URL_HOME_PAGE)

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)

    driver.find_element(*LOGIN_BUTTON).click()

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
    time.sleep(2)

    assert "/account/profile" in driver.current_url

