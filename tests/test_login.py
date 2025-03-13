import time
from conftest import driver
from helpers.locators import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, PERSONAL_ACCOUNT_BUTTON, REGISTER_LINK, EMAIL_FIELD
from helpers.constants import URL_FORGOT_PASS_PAGE, URL_REGISTRATION_PAGE, URL_HOME_PAGE

user_email = 'filipp_aslapov_19_011@mail.ru'
user_pass_succes_reg = 'Pass123'

class TestLogin:
    def test_login_from_button_log_in_to_your_account(self, driver):
        driver.get(URL_HOME_PAGE)
        time.sleep(1)

        driver.find_element(*LOGIN_BUTTON).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)

        driver.find_element(*LOGIN_BUTTON).click()
        time.sleep(1)

        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        email_field = driver.find_element(*EMAIL_FIELD)
        actual_email = email_field.get_attribute('value')

        assert actual_email == user_email

    def test_login_from_personal_account_button(self, driver):
        driver.get(URL_HOME_PAGE)
        time.sleep(1)

        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)

        driver.find_element(*LOGIN_BUTTON).click()
        time.sleep(1)

        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        email_field = driver.find_element(*EMAIL_FIELD)
        actual_email = email_field.get_attribute('value')

        assert actual_email == user_email


    def test_login_from_registration_form(self, driver):
        driver.get(URL_REGISTRATION_PAGE)
        time.sleep(1)

        driver.find_element(*REGISTER_LINK).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)

        driver.find_element(*LOGIN_BUTTON).click()
        time.sleep(1)

        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        email_field = driver.find_element(*EMAIL_FIELD)
        actual_email = email_field.get_attribute('value')

        assert actual_email == user_email


    def test_login_from_password_recovery_form(self, driver):
        driver.get(URL_FORGOT_PASS_PAGE)
        time.sleep(2)

        driver.find_element(*REGISTER_LINK).click()

        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)

        driver.find_element(*LOGIN_BUTTON).click()
        time.sleep(1)

        driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

        email_field = driver.find_element(*EMAIL_FIELD)
        actual_email = email_field.get_attribute('value')

        assert actual_email == user_email