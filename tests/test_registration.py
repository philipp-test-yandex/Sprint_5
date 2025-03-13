import time
from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.functions import generate_email_and_login
from helpers.locators import LOGIN_BUTTON,REGISTER_LINK,NAME_INPUT,LOGIN_EMAIL_INPUT,LOGIN_PASSWORD_INPUT, ERROR_MESSAGE, REGISTER_BUTTON
from helpers.constants import  URL_HOME_PAGE

class TestRegistration:
    def test_successful_registration(self, driver):
        user_name, user_email = generate_email_and_login()
        user_pass_succes_reg = 'Pass123'

        driver.get(URL_HOME_PAGE)
        time.sleep(1)

        driver.find_element(*LOGIN_BUTTON).click()
        driver.find_element(*REGISTER_LINK).click()

        driver.find_element(*NAME_INPUT).send_keys(user_name)
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)

        button_reg = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(REGISTER_BUTTON))
        driver.execute_script("arguments[0].click();", button_reg)

        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )

        assert "login" in driver.current_url

    def test_password_contains_less_than_6_characters(self, driver):
        user_name, user_email = generate_email_and_login()
        user_pass_less_6_char = 'pas'

        driver.get(URL_HOME_PAGE)
        time.sleep(1)

        driver.find_element(*LOGIN_BUTTON).click()
        driver.find_element(*REGISTER_LINK).click()

        driver.find_element(*NAME_INPUT).send_keys(user_name)
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_less_6_char)

        driver.find_element(*REGISTER_BUTTON).click()

        error_message = driver.find_element(*ERROR_MESSAGE).text
        assert "Некорректный пароль" in error_message