from conftest import driver
from conftest import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, PERSONAL_ACCOUNT_BUTTON
import time

user_email = 'filipp_aslapov_19_015@mail.ru'
user_pass_succes_reg = 'Pass123'

def test_click_through_personal_account(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)

    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)

    driver.find_element(*LOGIN_BUTTON).click()

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()
    time.sleep(2)

    assert "/account/profile" in driver.current_url

